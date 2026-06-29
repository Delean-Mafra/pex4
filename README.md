# Projeto de Extensão IV · Ciência de Dados
**Autor:** Delean Plince Mafra  
**Centro Universitário União das Américas Descomplica**  
**Ano:** 2026  

---

## Sobre o Projeto e Desenvolvimento das Atividades
Este projeto de extensão foi desenvolvido em parceria com uma organização parceira, com foco na melhoria da análise financeira através de técnicas de Ciência de Dados.  

O principal objetivo foi transformar dados financeiros em informações visuais e estratégicas, facilitando a tomada de decisão.

---

## Planejamento da Coleta de Dados e Problema Identificado
- Definição das fontes de informação: APIs corporativas e base de dados interna.  
- Problema identificado: baixa visibilidade das informações financeiras (contas a pagar e a receber).  
- Limitação dos relatórios tradicionais: dados predominantemente textuais e tabulares, dificultando a identificação de tendências e sazonalidades.  

---

## Coleta de Informações
- Dados obtidos via **API corporativa** e banco de dados relacional.  
- Ferramentas utilizadas: **Visual Studio Code**, **Python**, biblioteca **FDB** e extensão **SQLTools**.  
- Segurança: credenciais criptografadas e conformidade com a **LGPD** (apenas registros financeiros, sem dados pessoais).  

---

## Tecnologias Utilizadas
| Frameworks/Bibliotecas | Processamento/Visualização | Segurança/Utilidades |
|-------------------------|----------------------------|----------------------|
| Flask, Flask-WTF, WTForms | Pandas, NumPy, Matplotlib | Cryptography, OpenCV, LXML |
| Werkzeug, FDB | pdfplumber, pikepdf | psutil, pyzbar, argparse |
| python-dateutil | CSV, datetime, decimal | secrets, hashlib, logging |
| pathlib, os, re | threading, subprocess, tempfile | zipfile, xml.etree.ElementTree |

---

## Organização e Análise dos Dados
- Dados estruturados, reduzindo necessidade de limpeza.  
- Extração com **SQL** e análise com **Python**.  
- Visualizações criadas com **Matplotlib** e **NumPy**: séries temporais, gráficos comparativos e análises de composição.  
- Desenvolvimento de aplicação web com **Flask**, integrando consultas, indicadores e dashboards interativos.  

---

## Produção do Relatório Técnico
- Relatório consolidando análises e visualizações.  
- Gráficos de evolução temporal, comparativos e tabelas de indicadores.  
- Informações técnicas sensíveis foram anonimizadas.  
- Resultados: maior rapidez na identificação de tendências e padrões financeiros.  

---

## Sistema Web e Soluções Desenvolvidas
- **DRE Financeiro Automatizado**: saldo por conta.  
- **Análise de Gastos por Categoria**: evolução mensal e variação percentual.  
- **Relatório de Lançamentos Duplicados**.  
- **Conciliação Bancária (OFX)**.  
- **Extrator de Dados de Boletos (PDF)**.  
- **Análise de Financiamento**: evolução dos juros.  
- **Relatório de Gastos por Período**.  
- **Confronto IRRF**: comparação Receita Federal vs. registros internos.  

---

## Resultados Obtidos e Melhorias Futuras
- Maior visibilidade financeira e redução do tempo de análise manual.  
- Dados mais claros e visuais, apoiando decisões estratégicas.  
- Identificação de padrões históricos de fluxo de caixa.  
- **Perspectivas Futuras**: modelos preditivos, análises estatísticas avançadas e alertas automáticos.  

---

## Desafios Enfrentados
- Transformar grande volume de dados financeiros em gráficos simples e objetivos.  
- Garantir segurança da informação (criptografia e ofuscação).  
- Cumprir rigorosamente a **LGPD**.  

---

## Referências Principais
- [Flask](https://flask.palletsprojects.com/)  
- [Flask-WTF](https://flask-wtf.readthedocs.io/)  
- [WTForms](https://wtforms.readthedocs.io/)  
- [Werkzeug](https://werkzeug.palletsprojects.com/)  
- [FDB](https://pypi.org/project/fdb/)  
- [Pandas](https://pandas.pydata.org/docs/)  
- [Matplotlib](https://matplotlib.org/stable/contents.html)  
- [NumPy](https://numpy.org/doc/)  
- [Cryptography](https://cryptography.io/)  
- [OpenCV](https://docs.opencv.org/)  
- [LXML](https://lxml.de/)  
- [pdfplumber](https://github.com/jsvine/pdfplumber)  
- [pikepdf](https://pikepdf.readthedocs.io/)  
- [psutil](https://psutil.readthedocs.io/)  
- [pyzbar](https://pypi.org/project/pyzbar/)  
- [pyperclip](https://pyperclip.readthedocs.io/)  
- [argparse](https://docs.python.org/3/library/argparse.html)  
- [datetime](https://docs.python.org/3/library/datetime.html)  
- [decimal](https://docs.python.org/3/library/decimal.html)  
- [hashlib](https://docs.python.org/3/library/hashlib.html)  
- [logging](https://docs.python.org/3/library/logging.html)  
- [os](https://docs.python.org/3/library/os.html)  
- [pathlib](https://docs.python.org/3/library/pathlib.html)  
- [re](https://docs.python.org/3/library/re.html)  
- [secrets](https://docs.python.org/3/library/secrets.html)  
- [shutil](https://docs.python.org/3/library/shutil.html)  
- [string](https://docs.python.org/3/library/string.html)  
- [subprocess](https://docs.python.org/3/library/subprocess.html)  
- [sys](https://docs.python.org/3/library/sys.html)  
- [tempfile](https://docs.python.org/3/library/tempfile.html)  
- [threading](https://docs.python.org/3/library/threading.html)  
- [time](https://docs.python.org/3/library/time.html)  
- [traceback](https://docs.python.org/3/library/traceback.html)  
- [typing](https://docs.python.org/3/library/typing.html)  
- [warnings](https://docs.python.org/3/library/warnings.html)  
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)  
- [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)  
- [zipfile](https://docs.python.org/3/library/zipfile.html)  
