# 3. Carga (L)
def load_data(dataframe, output_path):
    import sqlite3 as sql
    import pandas as pd

    print("----------------------CARGA----------------------\n")

    # Criar um banco SQLite (arquivo vendas.db). (Dani)
    conexao = sql.connect('vendas.db')
    print("Banco de dados 'vendas.db' criado/conectado com sucesso. \n\n")


    # Salvar os dados tratados em uma tabela tb_vendas. (Michelle) (Andrea)
    dataframe.to_sql("tb_vendas", conexao, if_exists="replace", index=False)
    print("Dados carregados na tabela 'tb_vendas' do banco de dados 'vendas.db'.\n\n")


    # Criar uma segunda tabela tb_clientes contendo apenas clientes únicos. (Alana)
    df_clientes = dataframe[["cliente"]].drop_duplicates().reset_index(drop=True)
    df_clientes.to_sql("tb_clientes", conexao, if_exists="replace", index=False)
    print("Tabela 'tb_clientes' criada com clientes únicos no banco de dados 'vendas.db'.\n\n")


    # Relacionar tb_vendas com tb_clientes via chave estrangeira. (Ana)
    dataframe = dataframe.merge(df_clientes, on="cliente", how="left")
    print("Relacionamento lógico entre tb_vendas e tb_clientes criado (coluna: cliente). \n\n")

    # Escrever uma consulta SQL que mostre: total de vendas por categoria. (Vitória)
    query = """
        SELECT
            categoria,
            SUM(valor_total) AS total_vendas
        FROM tb_vendas
        GROUP BY categoria;
    """

    df_resultado = pd.read_sql_query(query, conexao)
    print("Resultado da consulta SQL - Total de vendas por categoria:\n")
    print(df_resultado.to_string())


    # Adicional gerar um relatório em arquivo texto com um resumo do banco de dados.
    print("\n\nGerando relatório do banco de dados...")
    print("Relatório gerado com sucesso: relatorio_banco_de_dados.txt\n")
    
    arquivo_saida="relatorio_banco_de_dados.txt"
    tabelas = pd.read_sql_query(
        "SELECT name FROM sqlite_master WHERE type='table';", conexao
    )

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(f"📄 RELATÓRIO DO BANCO: vendas.db\n")
        f.write("="*60 + "\n\n")
        f.write("Tabelas encontradas:\n")
        f.write(str(tabelas) + "\n\n")

        # Para cada tabela, exibir resumo e 15 primeiros registros
        for tabela in tabelas['name']:
            f.write(f"🗂️ Tabela: {tabela}\n")
            f.write("-"*60 + "\n")

            # Esquema (colunas e tipos)
            schema = pd.read_sql_query(f"PRAGMA table_info({tabela});", conexao)
            f.write("📋 Estrutura:\n")
            f.write(schema.to_string(index=False) + "\n\n")

            # Primeiras linhas
            df_preview = pd.read_sql_query(f"SELECT * FROM {tabela} LIMIT 30;", conexao)
            f.write("🔎 Primeiros registros:\n")
            f.write(df_preview.to_string(index=False) + "\n\n")

            # Contagem de registros
            count = pd.read_sql_query(f"SELECT COUNT(*) AS total FROM {tabela};", conexao)
            f.write(f"📊 Total de registros: {count['total'][0]}\n")
            f.write("="*60 + "\n\n")

    conexao.close()
