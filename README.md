# Projeto de Extensão IV - Ciência de Dados
**Autor:** Delean Plince Mafra  
**Instituição:** Centro Universitário União das Américas Descomplica  
**Ano:** 2026

---

## 📌 Sobre o Projeto e Desenvolvimento das Atividades
Este projeto de extensão foi desenvolvido em parceria com uma organização parceira, com foco na melhoria da análise financeira através de técnicas de Ciência de Dados.

Para dar início ao projeto, preenchi a Carta de Apresentação e selecionei a instituição parceira para a realização das atividades. Após a apresentação da proposta e a obtenção da autorização formal por meio do Termo de Autorização para Realização das Atividades Extensionistas, iniciei oficialmente o desenvolvimento do projeto. O principal objetivo foi transformar dados financeiros em informações visuais e estratégicas, facilitando a tomada de decisão.

## 📊 Planejamento da Coleta de Dados e Problema Identificado
A primeira etapa consistiu na elaboração de um plano de coleta de dados, no qual defini as fontes de informação que seriam utilizadas durante o projeto. Foram considerados dados obtidos por meio de interfaces de programação de aplicações (APIs) disponibilizadas pela organização, bem como informações provenientes de sua base de dados interna.

Durante essa fase, identifiquei as variáveis relevantes e os fatores que influenciavam diretamente os problemas enfrentados pela organização. A análise inicial evidenciou que a principal dificuldade estava relacionada à baixa visibilidade das informações financeiras referentes às contas a pagar e às contas a receber.

Embora a organização já dispusesse de relatórios financeiros tradicionais e da Demonstração do Resultado do Exercício (DRE), esses documentos apresentavam os dados de forma predominantemente textual e tabular, dificultando a identificação de tendências, sazonalidades e variações das receitas e despesas ao longo do tempo. Essa limitação comprometia a agilidade e a qualidade do processo de tomada de decisão pelos gestores.

## 🧠 Coleta de Informações
A coleta das informações foi realizada utilizando os recursos disponibilizados pela própria organização. Os dados estruturados foram obtidos por meio da API corporativa, responsável pelo acesso às informações armazenadas no banco de dados relacional utilizado pela empresa.

A organização autorizou o acesso à estrutura do banco de dados para fins exclusivamente acadêmicos e de desenvolvimento da solução proposta. Embora o ambiente utilizasse uma ferramenta específica para consultas ao banco de dados, optei por utilizar o **Visual Studio Code** em conjunto com **Python**, empregando a biblioteca **FDB** para comunicação com o banco de dados e a extensão **SQLTools** para desenvolvimento e validação das consultas SQL.

Como medida adicional de segurança da informação, desenvolvi uma biblioteca responsável por realizar a leitura automática das configurações de conexão existentes nos arquivos de configuração utilizados pela organização. As credenciais passaram a ser tratadas de forma criptografada, evitando sua exposição direta no código-fonte e reduzindo o risco de vazamento de informações sensíveis.

Para garantir conformidade com a **Lei Geral de Proteção de Dados (LGPD)**, limitei a coleta exclusivamente aos registros financeiros necessários para a execução do projeto. Não foram acessados ou processados dados pessoais de clientes, fornecedores ou colaboradores.

## ⚙️ Tecnologias Utilizadas
*   Flask
*   Flask-WTF
*   WTForms
*   Werkzeug
*   fdb
*   pandas
*   python-dateutil
*   matplotlib
*   pdfplumber
*   pikepdf
*   psutil
*   lxml
*   cryptography
*   cv2 (OpenCV)
*   numpy
*   pyzbar
*   pyperclip
*   argparse
*   base64
*   collections
*   csv
*   dataclasses
*   datetime
*   decimal
*   hashlib
*   io
*   logging
*   os
*   pathlib
*   re
*   secrets
*   shutil
*   string
*   subprocess
*   sys
*   tempfile
*   threading
*   time
*   traceback
*   typing
*   warnings
*   webbrowser
*   xml.etree.ElementTree
*   zipfile

## 📈 Organização e Análise dos Dados
Os dados disponibilizados pela organização já se encontravam estruturados, reduzindo significativamente a necessidade de procedimentos de limpeza e transformação. Dessa forma, concentrei os esforços na organização estratégica das informações e na construção de análises capazes de gerar conhecimento útil para a organização.

As atividades foram desenvolvidas utilizando **SQL** para extração das informações e **Python** para processamento, análise e apresentação dos resultados. As informações obtidas foram transformadas em representações gráficas por meio das bibliotecas **Matplotlib** e **NumPy**, possibilitando a criação de séries temporais, gráficos comparativos e análises de composição das despesas e receitas. 

Além da geração dos gráficos, desenvolvi uma aplicação web utilizando o framework **Flask**, responsável por integrar as consultas, os indicadores e as representações visuais em painéis interativos. Essa abordagem permitiu que os dados fossem consultados de forma dinâmica, oferecendo aos gestores uma visão consolidada das informações financeiras.

## 📄 Produção do Relatório Técnico
Após a conclusão das etapas de coleta, organização e análise dos dados, elaborei um relatório técnico para consolidar o trabalho e documentar os resultados. Por questões de segurança da informação, a organização pediu para **anonimizar informações técnicas sensíveis**, omitindo nomes internos do banco de dados e estruturas específicas.

O relatório incluiu gráficos de evolução temporal, comparativos entre períodos e tabelas consolidadas. As análises demonstraram que a utilização de painéis interativos proporciona maior rapidez na identificação de tendências financeiras e amplia a capacidade de acompanhamento dos indicadores ao longo do tempo. Como resultado, a organização passou a dispor de uma solução capaz de subsidiar o planejamento financeiro com base em evidências.

## 🌐 Sistema Web e Soluções Desenvolvidas
Foi criada uma aplicação web com Flask contendo dashboards interativos e consultas dinâmicas. Soluções integradas:

*   **DRE Financeiro Automatizado:** Painéis para visualização do resultado e saldo por conta.
*   **Análise de Gastos por Categoria:** Evolução dos gastos mensais, variação percentual e detalhamento.
*   **Relatório de Lançamentos Duplicados:** Ferramenta para localizar registros financeiros duplicados.
*   **Conciliação Bancária (OFX):** Compara lançamentos bancários com o banco de dados.
*   **Extrator de Dados de Boletos:** Upload de PDFs com extração automática de dados para o sistema.
*   **Análise de Financiamento:** Acompanhamento da evolução e variação dos juros.
*   **Relatório de Gastos:** Filtros por período e detalhamento de centros de custos.
*   **Confronto IRRF:** Comparação de valores retidos na Receita Federal vs registros internos.

## ✅ Resultados Obtidos e Melhorias Futuras
*   Maior visibilidade financeira e redução drástica do tempo de análise manual.
*   Dados mais claros e visuais para tomada de decisão.
*   Identificação de padrões históricos de fluxo de caixa.
*   **Perspectivas Futuras:** Implementação de modelos preditivos e alertas automáticos.

## 🚧 Desafios Enfrentados
*   Transformar grandes volumes de dados complexos em gráficos simples e objetivos.
*   Garantir a segurança da informação (criptografia e ofuscação de infraestrutura).
*   Respeitar estritamente as diretrizes da LGPD.

## 📚 Referências Principais
*   [Flask](https://flask.palletsprojects.com/)
*   [Flask-WTF](https://flask-wtf.readthedocs.io/)
*   [WTForms](https://wtforms.readthedocs.io/)
*   [Werkzeug](https://werkzeug.palletsprojects.com/)
*   [fdb](https://pypi.org/project/fdb/)
*   [pandas](https://pandas.pydata.org/docs/)
*   [python-dateutil](https://dateutil.readthedocs.io/)
*   [matplotlib](https://matplotlib.org/stable/contents.html)
*   [pdfplumber](https://github.com/jsvine/pdfplumber)
*   [pikepdf](https://pikepdf.readthedocs.io/)
*   [psutil](https://psutil.readthedocs.io/)
*   [lxml](https://lxml.de/)
*   [cryptography](https://cryptography.io/)
*   [cv2 (OpenCV)](https://docs.opencv.org/)
*   [numpy](https://numpy.org/doc/)
*   [pyzbar](https://pypi.org/project/pyzbar/)
*   [pyperclip](https://pyperclip.readthedocs.io/)
*   [Documentação Python (Bibliotecas Padrão)](https://docs.python.org/3/library/)

---
**Projeto de Extensão IV • Ciência de Dados • 2026**  
**Autor:** Delean Plince Mafra
