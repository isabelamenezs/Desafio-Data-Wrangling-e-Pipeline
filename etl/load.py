--3. Carga (L)


---Criar um banco SQLite (arquivo vendas.db). (Dani)

import sqlite3 as sql
conexao = sql.connect('vendas.db')
print("Banco de dados criado com sucesso!")


---Salvar os dados tratados em uma tabela chamada tb_vendas. (Michelle) (Andrea)




--Desafio Extra:
---Criar uma segunda tabela tb_clientes contendo apenas clientes únicos. (Alana)

tabela_vendas = sqlite3.connect("vendas.db")
df_clientes = df_vendas[["cliente"]].drop_duplicates().reset_index(drop=True)
df_clientes.to_sql("tb_clientes", tabela_vendas, if_exists="replace", index=False)
tabela_vendas.close()
