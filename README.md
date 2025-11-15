# azure-ml-automl-daily-bike-share
Pipeline de regressão com AutoML no Azure ML usando o dataset Daily Bike Share, com preparação de dados em UTF-8 e consumo via API

🚴‍♂️ Azure Machine Learning – AutoML com o Dataset Daily Bike Share

Este repositório documenta um projeto completo utilizando Azure Machine Learning e AutoML para prever a quantidade diária de bicicletas alugadas (Daily Bike Share).
Durante o laboratório oficial, ocorreram problemas de encoding e leitura do dataset via URL.
Aqui está a versão corrigida, funcional e estruturada de forma profissional, ideal para estudos de AI-900 e para uso como portfólio.

🎯 Objetivos do Projeto

- Corrigir o dataset original (encoding, schema e leitura).
- Criar um Data Asset Tabular UTF-8 no Azure ML usando upload local.
- Executar um experimento AutoML de regressão.
- Identificar automaticamente o melhor modelo.
- Criar e consumir um endpoint via API usando Python.
- Organizar o repositório de forma clara e profissional.

🧹 Correção e Preparação do Dataset

O dataset do laboratório gerava o erro:
TextFile-InvalidEncoding

Solução adotada:

1. Abrir o arquivo do Microsoft Learn no VS Code.
2. Converter para encoding UTF-8.
2. Salvar como: daily-bike-share.csv

Esse arquivo corrigido foi então importado no Azure Machine Learning.

📤 Criação do Data Asset no Azure ML

Configurações usadas:

- Tipo: Tabular
- Data source: From local files
- Delimiter: Comma
- Encoding: UTF-8
- Header: First line has headers

O schema foi carregado corretamente, incluindo a coluna-alvo rentals.

🤖 Execução do AutoML

- Task: Regression
- Dataset: daily-bike-share
- Target column: rentals
- Validation: Automatic
- Compute cluster: Standard_DS2_v2

O Azure ML avaliou diversos modelos (LightGBM, RandomForest, XGBoost, ElasticNet, etc.) e escolheu automaticamente o modelo com melhor Normalized RMSE.

🧪 Arquivo para Teste do Endpoint
Local: data/sample_input.json

🐍 Script Python para consumir o modelo
Local: scripts/consume_endpoint.py

📂 Estrutura final do repositório

azure-ml-automl-daily-bike-share/
│
├── data/
│   ├── daily-bike-share.csv
│   └── sample_input.json
│
├── scripts/
│   └── consume_endpoint.py
│
├── notebooks/
│   └── README-notebook.md
│
├── .gitignore
└── README.md
👤 Autor

Cláudio Menezes Santos
Estudos de Azure AI Fundamentals (AI-900)
Projeto prático usando Azure Machine Learning + AutoML
