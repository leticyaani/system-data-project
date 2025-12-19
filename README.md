# System Data Collector & Analyzer 📊

Este projeto demonstra a construção de um pipeline de dados completo (ETL) para coleta, armazenamento e análise de informações de hardware e sistema operacional em tempo real.

## 🎯 Objetivo
Desenvolver uma estrutura profissional de ingestão de dados para monitoramento de ambiente, utilizando Python e bibliotecas fundamentais de Data Science.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Análise de Dados:** Pandas
- **Ambiente:** Linux (WSL2 / Ubuntu)
- **Versionamento:** Git & GitHub

## 🔄 Fluxo de Dados (Pipeline)
1. **Extração (Extract):** O script `collect_data.py` utiliza a biblioteca `platform` para capturar métricas do sistema.
2. **Transformação/Carga (Load):** Os dados são estruturados em um dicionário e persistidos de forma incremental em um arquivo `system_data.csv`.
3. **Análise (Analysis):** O script `analyze_data.py` consome o dataset via Pandas, gerando insights sobre o histórico de execuções.

## 📁 Estrutura do Projeto
- `collect_data.py`: Engine de coleta de dados.
- `analyze_data.py`: Script de processamento e análise.
- `data/`: Diretório que armazena o dataset (CSV).
- `requirements.txt`: Dependências do projeto.

## 🚀 Como executar
1. Clone o repositório.
2. Crie um ambiente virtual: `python3 -m venv .venv`.
3. Instale as dependências: `pip install pandas`.
4. Execute a coleta: `python3 collect_data.py`.
5. Veja a análise: `python3 analyze_data.py`.

---
**Status do Projeto:** Em desenvolvimento (Próximo passo: Visualização gráfica com Matplotlib/Seaborn).
