from __future__ import annotations

import importlib.util
import os
from dataclasses import dataclass
from pathlib import Path
import re
import sys
import threading
import webbrowser
from typing import Any

from flask import Flask, redirect, render_template_string, url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from werkzeug.wrappers import Response


BASE_DIR = Path(__file__).resolve().parent
NO_FB_DIR = BASE_DIR / "no_fb"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5015


if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if NO_FB_DIR.exists() and str(NO_FB_DIR) not in sys.path:
    sys.path.insert(0, str(NO_FB_DIR))

os.chdir(BASE_DIR)


@dataclass(frozen=True)
class MountedApp:
    slug: str
    title: str
    group: str
    description: str
    file_path: Path
    prefix: str
    loaded: bool = False
    error: str | None = None


APP_SPECS: tuple[dict[str, str], ...] = (
    {
        "slug": "ofx",
        "title": "Conciliação Bancária",
        "group": "Financeiro",
        "description": "Importação de extratos OFX e conciliação automática de lançamentos financeiros corporativos.",
        "file": "db.conciador_ofx.py",
    },
    {
        "slug": "boletos",
        "title": "Gestão de Faturas",
        "group": "Financeiro",
        "description": "Processamento e atualização de cobranças empresariais e despesas operacionais.",
        "file": "db_app_boleto.py",
    },
    {
        "slug": "dre",
        "title": "DRE Gerencial",
        "group": "Controladoria",
        "description": "Demonstração de resultados financeiros, painéis mensais e acompanhamento de fluxo de caixa.",
        "file": "db_dre.py",
    },
    {
        "slug": "gastos",
        "title": "Dashboard de Despesas",
        "group": "Controladoria",
        "description": "Análise visual de despesas corporativas por centro de custo e período fiscal.",
        "file": "db_graficos_gastos.py",
    },
    {
        "slug": "financiamento",
        "title": "Gestão de Passivos",
        "group": "Controladoria",
        "description": "Acompanhamento histórico de amortizações e variações percentuais de passivos da organização.",
        "file": "db_financeiamento.py",
    },
    {
        "slug": "relatorio-gastos",
        "title": "Relatório Gerencial de Despesas",
        "group": "Relatórios",
        "description": "Relatório tabular de despesas operacionais por período e plano de contas contábil.",
        "file": "db_relatorio_gastos.py",
    },
    {
        "slug": "duplicados",
        "title": "Auditoria de Duplicidades",
        "group": "Auditoria e Compliance",
        "description": "Identificação e análise de lançamentos financeiros suspeitos ou duplicados.",
        "file": "db_registros_duplicados.py",
    },
    {
        "slug": "irrf",
        "title": "Auditoria de Retenções (IRRF/INSS)",
        "group": "Auditoria e Compliance",
        "description": "Confronto de retenções tributárias (IRRF/INSS) com registros dos sistemas e conciliação contábil.",
        "file": "db_irrf_confronto_web.py",
    },
)


class PrefixRewriteMiddleware:
    def __init__(self, app: Any, prefix: str) -> None:
        self.app = app
        self.prefix = prefix.rstrip("/")

    def __call__(self, environ: dict[str, Any], start_response: Any) -> Any:
        response = Response.from_app(self.app, environ)
        self._rewrite_location_header(response)
        self._rewrite_body(response)
        return response(environ, start_response)

    def _rewrite_location_header(self, response: Response) -> None:
        location = response.headers.get("Location")
        if not location:
            return
        if location.startswith("/") and not location.startswith(self.prefix + "/"):
            response.headers["Location"] = self.prefix + location

    def _rewrite_body(self, response: Response) -> None:
        content_type = response.headers.get("Content-Type", "")
        if not any(kind in content_type for kind in ("text/html", "javascript", "json")):
            return

        body = response.get_data(as_text=True)
        if not body:
            return

        prefix = self.prefix

        body = re.sub(
            r'((?:action|href|src)=["\'])(/(?!apps/|/|https?:|data:|mailto:|#))',
            rf"\1{prefix}\2",
            body,
        )

        body = re.sub(
            r"(fetch\(\s*[\"'`])(/(?!apps/|/|https?:))",
            rf"\1{prefix}\2",
            body,
        )

        body = re.sub(
            r"(url\(\s*[\"']?)(/(?!apps/|/|https?:|data:))",
            rf"\1{prefix}\2",
            body,
        )
        body = re.sub(
            r"((?:window\.)?location(?:\.href)?\s*=\s*[\"'])(/(?!apps/|/|https?:))",
            rf"\1{prefix}\2",
            body,
        )

        response.set_data(body)
        response.headers.pop("Content-Length", None)


def load_flask_app(spec: dict[str, str]) -> tuple[Any | None, MountedApp]:
    file_path = BASE_DIR / spec["file"]
    prefix = f"/apps/{spec['slug']}"
    metadata = MountedApp(
        slug=spec["slug"],
        title=spec["title"],
        group=spec["group"],
        description=spec["description"],
        file_path=file_path,
        prefix=prefix,
    )

    try:
        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado no diretório especificado: {file_path}")

        module_name = f"enterprise_app_{spec['slug'].replace('-', '_')}"
        import_spec = importlib.util.spec_from_file_location(module_name, file_path)
        if not import_spec or not import_spec.loader:
            raise RuntimeError(f"Falha ao carregar o módulo: {file_path}")

        module = importlib.util.module_from_spec(import_spec)
        sys.modules[module_name] = module
        import_spec.loader.exec_module(module)

        child_app = getattr(module, "app", None)
        if child_app is None:
            raise RuntimeError("O módulo não possui uma instância Flask válida instanciada como 'app'.")

        child_app.config["APPLICATION_ROOT"] = prefix
        child_app.config["PREFERRED_URL_SCHEME"] = "http"

        return PrefixRewriteMiddleware(child_app, prefix), MountedApp(
            slug=metadata.slug,
            title=metadata.title,
            group=metadata.group,
            description=metadata.description,
            file_path=metadata.file_path,
            prefix=metadata.prefix,
            loaded=True,
            error=None,
        )
    except Exception as exc:
        return None, MountedApp(
            slug=metadata.slug,
            title=metadata.title,
            group=metadata.group,
            description=metadata.description,
            file_path=metadata.file_path,
            prefix=metadata.prefix,
            loaded=False,
            error=str(exc),
        )


hub = Flask(__name__)
hub.secret_key = "enterprise_portal_secret_2026"


@hub.route("/")
def index() -> str:
    loaded_apps = [app for app in mounted_apps if app.loaded]
    failed_apps = [app for app in mounted_apps if not app.loaded]
    groups = sorted({app.group for app in loaded_apps})
    first_slug = loaded_apps[0].slug if loaded_apps else ""
    return render_template_string(
        DASHBOARD_TEMPLATE,
        loaded_apps=loaded_apps,
        failed_apps=failed_apps,
        groups=groups,
        first_slug=first_slug,
        total=len(mounted_apps),
    )


@hub.route("/abrir/<slug>")
def abrir(slug: str) -> Any:
    target = next((app for app in mounted_apps if app.slug == slug and app.loaded), None)
    if not target:
        return redirect(url_for("index"))
    return redirect(target.prefix + "/")


def build_application() -> Any:
    mounts: dict[str, Any] = {}
    loaded: list[MountedApp] = []

    for spec in APP_SPECS:
        child_app, metadata = load_flask_app(spec)
        loaded.append(metadata)
        if child_app is not None:
            mounts[metadata.prefix] = child_app

    globals()["mounted_apps"] = loaded
    return DispatcherMiddleware(hub, mounts)


DASHBOARD_TEMPLATE = r"""
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Enterprise Application Hub</title>
  <style>
    :root {
      --bg: #f4f6f8;
      --panel: #ffffff;
      --panel-2: #eef3f7;
      --text: #17202a;
      --muted: #64748b;
      --line: #d7dee7;
      --primary: #0056b3;
      --primary-2: #004085;
      --danger: #b42318;
      --warning-bg: #fff7ed;
      --warning-line: #fed7aa;
      --radius: 8px;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      height: 100vh;
      overflow: hidden;
    }

    .shell {
      display: grid;
      grid-template-columns: 310px 1fr;
      height: 100vh;
      min-height: 0;
    }

    .sidebar {
      background: var(--panel);
      border-right: 1px solid var(--line);
      display: flex;
      flex-direction: column;
      min-height: 0;
    }

    .brand {
      padding: 18px 18px 14px;
      border-bottom: 1px solid var(--line);
    }

    .brand h1 {
      margin: 0;
      font-size: 22px;
      line-height: 1.15;
      font-weight: 700;
    }

    .brand p {
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.4;
    }

    .status {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-top: 12px;
    }

    .metric {
      background: var(--panel-2);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 8px;
    }

    .metric strong {
      display: block;
      font-size: 18px;
    }

    .metric span {
      color: var(--muted);
      font-size: 12px;
    }

    .nav {
      overflow: auto;
      padding: 10px;
      min-height: 0;
    }

    .group-title {
      color: var(--muted);
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0;
      margin: 14px 8px 7px;
    }

    .tab-button {
      width: 100%;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 8px;
      align-items: center;
      border: 1px solid transparent;
      background: transparent;
      color: var(--text);
      text-align: left;
      border-radius: var(--radius);
      padding: 10px;
      cursor: pointer;
      min-height: 62px;
    }

    .tab-button:hover {
      background: #f8fafc;
      border-color: var(--line);
    }

    .tab-button.active {
      background: #e6f0fa;
      border-color: #b8daff;
      color: var(--primary-2);
    }

    .tab-title {
      display: block;
      font-size: 14px;
      font-weight: 700;
      line-height: 1.2;
    }

    .tab-desc {
      display: block;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.3;
      margin-top: 3px;
    }

    .open-link {
      color: var(--primary);
      text-decoration: none;
      font-size: 12px;
      font-weight: 700;
    }

    .content {
      display: grid;
      grid-template-rows: auto 1fr;
      min-width: 0;
      min-height: 0;
    }

    .toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px 16px;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
    }

    .toolbar-main {
      min-width: 0;
    }

    .toolbar h2 {
      margin: 0;
      font-size: 18px;
      line-height: 1.2;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .toolbar p {
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.3;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .toolbar-actions {
      display: flex;
      gap: 8px;
      flex: 0 0 auto;
    }

    .btn {
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--text);
      text-decoration: none;
      border-radius: var(--radius);
      padding: 8px 10px;
      font-size: 13px;
      cursor: pointer;
      white-space: nowrap;
    }

    .btn.primary {
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
    }

    .frame-wrap {
      min-height: 0;
      padding: 12px;
    }

    iframe {
      width: 100%;
      height: 100%;
      display: none;
      border: 1px solid var(--line);
      background: #fff;
      border-radius: var(--radius);
    }

    iframe.active {
      display: block;
    }

    .empty, .failures {
      padding: 20px;
    }

    .failures {
      border-top: 1px solid var(--line);
      background: var(--warning-bg);
      max-height: 180px;
      overflow: auto;
    }

    .failures h3 {
      margin: 0 0 8px;
      font-size: 14px;
      color: var(--danger);
    }

    .failure {
      border: 1px solid var(--warning-line);
      background: #fff;
      border-radius: var(--radius);
      padding: 8px;
      margin-top: 8px;
      font-size: 12px;
      line-height: 1.35;
    }

    .failure strong {
      display: block;
      font-size: 13px;
    }

    .failure code {
      color: var(--danger);
      word-break: break-word;
    }

    @media (max-width: 900px) {
      body { overflow: auto; height: auto; }
      .shell {
        display: block;
        height: auto;
      }
      .sidebar {
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }
      .nav {
        display: flex;
        gap: 8px;
        overflow-x: auto;
        padding: 10px;
      }
      .group-title { display: none; }
      .tab-button {
        width: 220px;
        flex: 0 0 auto;
      }
      .content {
        height: calc(100vh - 210px);
        min-height: 560px;
      }
      .toolbar {
        align-items: flex-start;
        flex-direction: column;
      }
      .toolbar p {
        white-space: normal;
      }
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside class="sidebar">
      <div class="brand">
        <h1>Portal Corporativo</h1>
        <p>Plataforma centralizada para gestão de microsserviços internos.</p>
        <div class="status">
          <div class="metric">
            <strong>{{ loaded_apps|length }}</strong>
            <span>módulos ativos</span>
          </div>
          <div class="metric">
            <strong>{{ failed_apps|length }}</strong>
            <span>serviços inativos</span>
          </div>
        </div>
      </div>

      {% if loaded_apps %}
      <nav class="nav" aria-label="Aplicações Corporativas">
        {% for group in groups %}
          <div class="group-title">{{ group }}</div>
          {% for app in loaded_apps if app.group == group %}
            <button
              class="tab-button {% if app.slug == first_slug %}active{% endif %}"
              type="button"
              data-slug="{{ app.slug }}"
              data-title="{{ app.title }}"
              data-description="{{ app.description }}"
              data-url="{{ app.prefix }}/"
            >
              <span>
                <span class="tab-title">{{ app.title }}</span>
                <span class="tab-desc">{{ app.description }}</span>
              </span>
              <span class="open-link">abrir</span>
            </button>
          {% endfor %}
        {% endfor %}
      </nav>
      {% endif %}

      {% if failed_apps %}
      <section class="failures">
        <h3>Serviços Inativos</h3>
        {% for app in failed_apps %}
          <div class="failure">
            <strong>{{ app.title }}</strong>
            <span>{{ app.file_path.name }}</span><br>
            <code>{{ app.error }}</code>
          </div>
        {% endfor %}
      </section>
      {% endif %}
    </aside>

    <main class="content">
      <header class="toolbar">
        <div class="toolbar-main">
          <h2 id="currentTitle">Selecione um Módulo</h2>
          <p id="currentDescription">Os módulos corporativos são carregados no painel centralizado de forma integrada e isolada.</p>
        </div>
        <div class="toolbar-actions">
          <button class="btn" type="button" id="reloadBtn">Recarregar</button>
          <a class="btn primary" href="#" id="newTabLink" target="_blank" rel="noreferrer">Nova aba</a>
        </div>
      </header>

      <section class="frame-wrap">
        {% if loaded_apps %}
          {% for app in loaded_apps %}
            <iframe
              class="{% if app.slug == first_slug %}active{% endif %}"
              id="frame-{{ app.slug }}"
              data-slug="{{ app.slug }}"
              data-title="{{ app.title }}"
              data-description="{{ app.description }}"
              src="{{ app.prefix }}/"
              title="{{ app.title }}"
            ></iframe>
          {% endfor %}
        {% else %}
          <div class="empty">
            Nenhum módulo corporativo foi carregado. Verifique os logs de integração.
          </div>
        {% endif %}
      </section>
    </main>
  </div>

  <script>
    const buttons = Array.from(document.querySelectorAll('.tab-button'));
    const frames = Array.from(document.querySelectorAll('iframe[data-slug]'));
    const title = document.getElementById('currentTitle');
    const description = document.getElementById('currentDescription');
    const reloadBtn = document.getElementById('reloadBtn');
    const newTabLink = document.getElementById('newTabLink');

    let activeSlug = '{{ first_slug }}';

    function setActive(slug) {
      const button = buttons.find((item) => item.dataset.slug === slug);
      const frame = frames.find((item) => item.dataset.slug === slug);
      if (!button || !frame) return;

      activeSlug = slug;

      buttons.forEach((item) => item.classList.toggle('active', item.dataset.slug === slug));
      frames.forEach((item) => item.classList.toggle('active', item.dataset.slug === slug));

      title.textContent = button.dataset.title;
      description.textContent = button.dataset.description;
      newTabLink.href = button.dataset.url;
      window.history.replaceState(null, '', '#' + slug);
    }

    buttons.forEach((button) => {
      button.addEventListener('click', () => setActive(button.dataset.slug));
    });

    reloadBtn.addEventListener('click', () => {
      const frame = frames.find((item) => item.dataset.slug === activeSlug);
      if (frame) frame.contentWindow.location.reload();
    });

    const initialHash = window.location.hash.replace('#', '');
    if (initialHash && buttons.some((item) => item.dataset.slug === initialHash)) {
      setActive(initialHash);
    } else if (activeSlug) {
      setActive(activeSlug);
    }
  </script>
</body>
</html>
"""


mounted_apps: list[MountedApp] = []
application = build_application()


def open_browser() -> None:
    webbrowser.open_new(f"http://{DEFAULT_HOST}:{DEFAULT_PORT}/")


if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    print(f"Portal Corporativo rodando em http://{DEFAULT_HOST}:{DEFAULT_PORT}/")
    run_simple(DEFAULT_HOST, DEFAULT_PORT, application, use_debugger=False, use_reloader=False)
