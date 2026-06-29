Projeto de Extensão IV
📌 Sobre o Projeto e Desenvolvimento das Atividades
Este projeto de extensão foi desenvolvido em parceria com uma organização parceira, com foco na
melhoria da análise financeira através de técnicas de Ciência de Dados.
Para dar início ao projeto, preenchi a Carta de Apresentação e selecionei a instituição parceira para
a realização das atividades. Após a apresentação da proposta e a obtenção da autorização formal
por meio do Termo de Autorização para Realização das Atividades Extensionistas, iniciei
oficialmente o desenvolvimento do projeto. O principal objetivo foi transformar dados financeiros em
informações visuais e estratégicas, facilitando a tomada de decisão.
📊 Planejamento da Coleta de Dados e Problema Identificado
A primeira etapa consistiu na elaboração de um plano de coleta de dados, no qual defini as fontes de
informação que seriam utilizadas durante o projeto. Foram considerados dados obtidos por meio de
interfaces de programação de aplicações (APIs) disponibilizadas pela organização, bem como
informações provenientes de sua base de dados interna.
Durante essa fase, identifiquei as variáveis relevantes e os fatores que influenciavam diretamente os
problemas enfrentados pela organização. A análise inicial evidenciou que a principal dificuldade
estava relacionada à baixa visibilidade das informações financeiras referentes às contas a pagar e
às contas a receber.
Embora a organização já dispusesse de relatórios financeiros tradicionais e da Demonstração do
Resultado do Exercício (DRE), esses documentos apresentavam os dados de forma
predominantemente textual e tabular, dificultando a identificação de tendências, sazonalidades e
variações das receitas e despesas ao longo do tempo. Essa limitação comprometia a agilidade e a
qualidade do processo de tomada de decisão pelos gestores.
Ciência de Dados • Delean Plince Mafra
Centro Universitário União das Américas Descomplica

🧠 Coleta de Informações
A coleta das informações foi realizada utilizando os recursos disponibilizados pela própria
organização. Os dados estruturados foram obtidos por meio da API corporativa, responsável pelo
acesso às informações armazenadas no banco de dados relacional utilizado pela empresa.
A organização autorizou o acesso à estrutura do banco de dados para fins exclusivamente
acadêmicos e de desenvolvimento da solução proposta. Embora o ambiente utilizasse uma
ferramenta específica para consultas ao banco de dados, optei por utilizar o Visual Studio Code em
conjunto com Python, empregando a biblioteca FDB para comunicação com o banco de dados e a
extensão SQLTools para desenvolvimento e validação das consultas SQL.
Como medida adicional de segurança da informação, desenvolvi uma biblioteca responsável por
realizar a leitura automática das configurações de conexão existentes nos arquivos de configuração
utilizados pela organização. As credenciais passaram a ser tratadas de forma criptografada, evitando
sua exposição direta no código-fonte e reduzindo o risco de vazamento de informações sensíveis.
Para garantir conformidade com a Lei Geral de Proteção de Dados (LGPD), limitei a coleta
exclusivamente aos registros financeiros necessários para a execução do projeto. Não foram
acessados ou processados dados pessoais de clientes, fornecedores ou colaboradores, restringindo
a análise às informações relacionadas aos lançamentos financeiros utilizados na elaboração dos
indicadores e das visualizações.
⚙️ Tecnologias Utilizadas
Flask
Flask-WTF
WTForms
Werkzeug
fdb
pandas
python-dateutil
matplotlib
pdfplumber
pikepdf
psutil
lxml
cryptography
cv2 (OpenCV)
numpy
pyzbar
pyperclip
argparse

base64
collections
csv
dataclasses
datetime
decimal
hashlib
io
logging
os
pathlib
re
secrets
shutil
string
subprocess
sys
tempfile
threading
time
traceback
typing
warnings
webbrowser
xml.etree.ElementTree
zipfile
📈 Organização e Análise dos Dados
Os dados disponibilizados pela organização já se encontravam estruturados, reduzindo
significativamente a necessidade de procedimentos de limpeza e transformação. Dessa forma,
concentrei os esforços na organização estratégica das informações e na construção de análises
capazes de gerar conhecimento útil para a organização.
As atividades foram desenvolvidas utilizando SQL para extração das informações e Python para
processamento, análise e apresentação dos resultados. Entre as principais bibliotecas empregadas
destacam-se Flask, FDB, Pandas, NumPy, Matplotlib, Flask-WTF, WTForms, Werkzeug, Python-
Dateutil, Cryptography, LXML, OpenCV e outras bibliotecas auxiliares responsáveis por operações
de processamento, segurança, geração de arquivos e automação.
As informações obtidas foram transformadas em representações gráficas por meio das bibliotecas
Matplotlib e NumPy, possibilitando a criação de séries temporais, gráficos comparativos e análises
de composição das despesas e receitas. Essas visualizações facilitaram a identificação de
tendências, oscilações financeiras e fatores que impactavam diretamente o fluxo de caixa da
organização.
Além da geração dos gráficos, desenvolvi uma aplicação web utilizando o framework Flask,
responsável por integrar as consultas, os indicadores e as representações visuais em painéis

interativos. Essa abordagem permitiu que os dados fossem consultados de forma dinâmica,
oferecendo aos gestores uma visão consolidada das informações financeiras.
A etapa de análise ultrapassou o simples processamento técnico dos dados, buscando transformar
informações isoladas em conhecimento capaz de apoiar decisões estratégicas. O cruzamento das
informações permitiu compreender padrões de comportamento financeiro, identificar períodos de
maior concentração de despesas e acompanhar a evolução das receitas ao longo do tempo.
📄 Produção do Relatório Técnico
Após a conclusão das etapas de coleta, organização e análise dos dados, elaborei um relatório
técnico com o objetivo de consolidar todo o trabalho desenvolvido e documentar os principais
resultados obtidos. Por questões de segurança da informação, a organização pediu para anonimizar
informações técnicas sensíveis, omitindo nomes internos do banco de dados, estruturas específicas,
caminhos de arquivos e demais elementos que pudessem comprometer a infraestrutura tecnológica
da empresa. Dessa forma, foi possível apresentar toda a metodologia empregada sem expor
informações confidenciais.
O relatório foi estruturado a partir das análises realizadas e das visualizações desenvolvidas durante
o projeto. Foram incluídos gráficos de evolução temporal, comparativos entre períodos, análises de
receitas e despesas e tabelas consolidadas contendo os principais indicadores financeiros.
Complementando essas representações, elaborei descrições técnicas que contextualizam os
resultados encontrados e explicam sua importância para a gestão financeira da organização.
As análises demonstraram que a utilização de painéis interativos e relatórios gráficos proporciona
maior rapidez na identificação de tendências financeiras, reduz o tempo necessário para
interpretação das informações e amplia a capacidade de acompanhamento dos indicadores ao
longo do tempo. A comparação histórica também possibilitou identificar padrões que dificilmente
seriam percebidos utilizando apenas relatórios convencionais.
Como resultado, a organização passou a dispor de uma solução capaz de apoiar o processo de
tomada de decisão por meio da análise visual dos dados financeiros, permitindo identificar variações
de receitas e despesas, acompanhar a evolução do fluxo de caixa e subsidiar o planejamento
financeiro com base em evidências.
🌐 Sistema Web e Soluções Desenvolvidas
Foi criada uma aplicação web com Flask contendo dashboards interativos, visualização em tempo
real e consultas dinâmicas. Entre as soluções integradas no sistema estão:

DRE Financeiro Automatizado: Painéis completos para visualização do resultado e saldo por
conta.
Análise de Gastos por Categoria: Evolução dos gastos mensais, variação percentual e
detalhamento das contas.
Relatório de Lançamentos Duplicados: Ferramenta para localizar possíveis registros
financeiros duplicados no banco de dados.
Conciliação Bancária (OFX): Compara e concilia os lançamentos bancários (arquivo OFX) com
os lançamentos do banco de dados, acusando transações não encontradas.
Extrator de Dados de Boletos: Faz o upload de PDFs (condomínio, faculdade), extrai dados
automaticamente e atualiza diretamente no banco de dados, eliminando o lançamento manual.
Análise de Financiamento: Acompanha a evolução e variação percentual dos juros ao longo do
tempo.
Relatório de Gastos: Filtra valores por período, detalhando os centros de custos.
Confronto IRRF: Compara os valores de IRRF retidos na Receita Federal com os registros do
banco de dados interno.
✅ Resultados Obtidos e Melhorias Futuras
Maior visibilidade financeira e redução drástica do tempo de análise manual.
Dados mais claros e visuais, impulsionando a melhoria na tomada de decisão.
Identificação de padrões históricos de fluxo de caixa invisíveis em tabelas normais.
Perspectivas Futuras: Implementação de modelos preditivos, análises estatísticas avançadas e
criação de alertas automáticos financeiros no sistema web.
🚧 Desafios Enfrentados
Transformar dados e um grande volume de informações financeiras complexas em gráficos
simples, objetivos e de fácil interpretação para os gestores.
Garantir a segurança da informação durante todo o ciclo de vida do projeto (ex: criptografia de
credenciais via Python e ofuscação de infraestrutura).

Respeitar estritamente as diretrizes da LGPD, processando apenas registros financeiros sem
expor dados pessoais sensíveis.
📚 Referências Principais
Flask: https://flask.palletsprojects.com/
Flask-WTF: https://flask-wtf.readthedocs.io/
WTForms: https://wtforms.readthedocs.io/
Werkzeug: https://werkzeug.palletsprojects.com/
fdb: https://pypi.org/project/fdb/
pandas: https://pandas.pydata.org/docs/
python-dateutil: https://dateutil.readthedocs.io/
matplotlib: https://matplotlib.org/stable/contents.html
pdfplumber: https://github.com/jsvine/pdfplumber
pikepdf: https://pikepdf.readthedocs.io/
psutil: https://psutil.readthedocs.io/
lxml: https://lxml.de/
cryptography: https://cryptography.io/
cv2 (OpenCV): https://docs.opencv.org/
numpy: https://numpy.org/doc/
pyzbar: https://pypi.org/project/pyzbar/
pyperclip: https://pyperclip.readthedocs.io/
argparse: https://docs.python.org/3/library/argparse.html
base64: https://docs.python.org/3/library/base64.html
collections: https://docs.python.org/3/library/collections.html
csv: https://docs.python.org/3/library/csv.html
dataclasses: https://docs.python.org/3/library/dataclasses.html
datetime: https://docs.python.org/3/library/datetime.html
decimal: https://docs.python.org/3/library/decimal.html
hashlib: https://docs.python.org/3/library/hashlib.html

io: https://docs.python.org/3/library/io.html
logging: https://docs.python.org/3/library/logging.html
os: https://docs.python.org/3/library/os.html
pathlib: https://docs.python.org/3/library/pathlib.html
re: https://docs.python.org/3/library/re.html
secrets: https://docs.python.org/3/library/secrets.html
shutil: https://docs.python.org/3/library/shutil.html
string: https://docs.python.org/3/library/string.html
subprocess: https://docs.python.org/3/library/subprocess.html
sys: https://docs.python.org/3/library/sys.html
tempfile: https://docs.python.org/3/library/tempfile.html
threading: https://docs.python.org/3/library/threading.html
time: https://docs.python.org/3/library/time.html
traceback: https://docs.python.org/3/library/traceback.html
typing: https://docs.python.org/3/library/typing.html
warnings: https://docs.python.org/3/library/warnings.html
webbrowser: https://docs.python.org/3/library/webbrowser.html
xml.etree.ElementTree: https://docs.python.org/3/library/xml.etree.elementtree.html
zipfile: https://docs.python.org/3/library/zipfile.html
Projeto de Extensão IV • Ciência de Dados • 2026
Autor: Delean Plince Mafra

