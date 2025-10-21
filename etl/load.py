# 3. Carga (L)
def load_data(df, output_path):
  # Criar um banco SQLite (arquivo vendas.db). (Dani)
  import sqlite3 as sql
  conexao = sql.connect('vendas.db')
  print("Banco de dados criado com sucesso!")


  # Salvar os dados tratados em uma tabela tb_vendas. (Michelle) (Andrea)

  dataframe.to_sql("tb_vendas", conexao, if_exists="replace", index=False)

  conexao.close()


  ## Desafio Extra:
  # Criar uma segunda tabela tb_clientes contendo apenas clientes únicos. (Alana)

  conexao = sqlite3.connect("vendas.db")
  df_clientes = dataframe[["cliente"]].drop_duplicates().reset_index(drop=True)
  df_clientes.to_sql("tb_clientes", conexao, if_exists="replace", index=False)
  conexao.close()

  # Relacionar tb_vendas com tb_clientes via chave estrangeira. (Ana)

  # Escrever uma consulta SQL que mostre: total de vendas por categoria. (Vitória)

  SELECT categoria, SUM(valor_total) AS total_vendas
  FROM tb_vendas
  GROUP BY categoria;
