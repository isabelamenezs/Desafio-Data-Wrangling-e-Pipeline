**Desafio Data Wrangling & Pipeline de Dados**

Este projeto foi desenvolvido como parte do Bootcamp de Business Intelligence (2025) e tem como objetivo criar um pipeline de dados em Python para tratar e carregar um conjunto de dados de vendas online em um banco SQLite.

**Objetivo do Projeto**

A proposta é automatizar o processo ETL (Extração, Transformação e Carga) de um dataset bruto contendo inconsistências, aplicando técnicas de data wrangling e boas práticas de organização de código.

**Funcionalidades Implementadas**
🔹 1. Extração (extraction.py)

- Leitura do arquivo CSV bruto.

- Visualização inicial dos dados (head, tipos de colunas, valores nulos).

- Retorno de um DataFrame para as próximas etapas.

🔹 2. Transformação (transform.py)

- Padronização da coluna de data no formato YYYY-MM-DD.

- Substituição de valores nulos por "Não informado".

- Conversão de quantidades textuais para inteiros.

- Correção de preços negativos.

- Criação da coluna valor_total = quantidade * preco_unitario.

🔹 3. Carga (load.py)

- Criação de um banco de dados SQLite (vendas.db).

- Inserção dos dados tratados na tabela tb_vendas.

🔹 4. Pipeline Principal (pipeline.py)

- Importa as funções dos arquivos anteriores.

- Executa as etapas E → T → L de forma sequencial.

- Garante o fluxo automatizado de dados do CSV até o banco.

**Tecnologias Utilizadas**

Python 3.12+

Pandas

SQLite3 (ou SQLAlchemy)

Jupyter / VS Code / Google Colab (para testes e desenvolvimento)

**Como Executar o Projeto**
1. Clone o repositório:
git clone https://github.com/isabelamenezs/Desafio-Data-Wrangling-e-Pipeline
cd <Desafio-Data-Wrangling-e-Pipeline>

2. Instale as dependências:
pip install pandas sqlalchemy

3. Execute o pipeline:
python pipeline.py

4. Verifique o banco de dados:

Abra o arquivo vendas.db (pode usar o DB Browser for SQLite) e confirme se a tabela tb_vendas foi criada com os dados tratados.
