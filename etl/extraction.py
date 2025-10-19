--1. Leitura e Exploração Inicial

---1.	Leia o arquivo CSV e visualize as 5 primeiras linhas do dataset. (michelle) (isabela)
import pandas as pd
dataframe = pd.read_csv('vendas_raw.csv')
print(dataframe.head())

---2.	Verifique o número de linhas e colunas. (andrea)
contColuna = len(dataframe.axes[0])
contLinha = len(dataframe.axes[1]) 
print("Número de colunas:"+str(contColuna))
print("Número de linhas:"+str(contLinha))

---3.	Descubra o tipo de dados (dtype) de cada coluna. (alana)

tipo_colunas = dataframe.dtypes
print(tipo_colunas)

---4.	Conte os valores ausentes existentes em cada coluna. (ana)




--2. Seleção e Filtragem de Dados

---1.	Filtre apenas as linhas onde o preço unitário é maior que 100. (Isabela)

---2.	Ordene o dataset pelo valor do preço em ordem decrescente. (Amanda) (Alessa)
import pandas as pd

# Leitura do dataset
df = pd.read_csv('2lBCPRISD6UzKRFg5VZ1_vendas (3).csv')

# Ordenar pelo preço unitário em ordem decrescente
df_ordenado = df.sort_values(by='preco_unitario', ascending=False)

# Exibir as 5 primeiras linhas para verificação
print(df_ordenado.head())



