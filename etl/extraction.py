#1. Leitura e Exploração Inicial
import pandas as pd
def explore_data(filepath):
  #1.	Leia o arquivo CSV e visualize as 5 primeiras linhas do dataset.
  dataframe = pd.read_csv(filepath)
  print(dataframe.head(5))
  
  #2.	Verifique o número de linhas e colunas.
  contColuna = len(dataframe.axes[0])
  contLinha = len(dataframe.axes[1]) 
  print("Número de colunas:"+str(contColuna))
  print("Número de linhas:"+str(contLinha))

  #3.	Descubra o tipo de dados (dtype) de cada coluna.
  tipo_colunas = dataframe.dtypes
  print(tipo_colunas)

  #4.	Conte os valores ausentes existentes em cada coluna.
  valores_ausentes = dataframe.isnull().sum()
  
  # Exibir o resultado
  print("Valores ausentes por coluna:\n")
  print(valores_ausentes)

  #2. Seleção e Filtragem de Dados
  #1.	Filtre apenas as linhas onde o preço unitário é maior que 100.
  preco_maior_que_100 = dataframe['preco_unitario'] > 100
  print(dataframe[preco_maior_que_100])

  #2.	Ordene o dataset pelo valor do preço em ordem decrescente. 
  df_ordenado = dataframe.sort_values(by='preco_unitario', ascending=False)

  # Exibir as 5 primeiras linhas para verificação
  print(df_ordenado.head(5))

return dataframe

