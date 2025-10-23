
def extract_data(filepath):

  import pandas as pd

  print("\n\n---------------------EXTRAÇÃO--------------------\n")

  #1.	Leia o arquivo CSV e visualize as 5 primeiras linhas do dataset.
  dataframe = pd.read_csv(filepath)
  print("Visualização das 5 primeiras linhas do dataset:")
  print(dataframe.head(5).to_string() + "\n\n")
  
  #2.	Verifique o número de linhas e colunas.
  contColuna = len(dataframe.axes[0])
  contLinha = len(dataframe.axes[1]) 
  print("Número de colunas:"+str(contColuna))
  print("Número de linhas:"+str(contLinha) + "\n\n")

  #3.	Descubra o tipo de dados (dtype) de cada coluna.
  tipo_colunas = dataframe.dtypes
  print("Tipo de dados por coluna:\n")
  print(tipo_colunas)
  print("\n\n")

  #4.	Conte os valores ausentes existentes em cada coluna.
  valores_ausentes = dataframe.isnull().sum()
  
  # Exibir o resultado
  print("Valores ausentes por coluna:\n")
  print(valores_ausentes)
  print("\n\n")


  #2. Seleção e Filtragem de Dados
  #1.	Filtre apenas as linhas onde o preço unitário é maior que 100.
  preco_maior_que_100 = dataframe['preco_unitario'] > 100
  print("Linhas dos 5 primeiros onde o preço unitário é maior que 100: \n")
  print(dataframe[preco_maior_que_100].head(5).to_string())
  print("\n\n")

  #2.	Ordene o dataset pelo valor do preço em ordem decrescente. 
  df_ordenado = dataframe.sort_values(by='preco_unitario', ascending=False)

  # Exibir as 5 primeiras linhas para verificação
  print("Dataset ordenado pelo preço unitário em ordem decrescente:\n")
  print(df_ordenado.head(5))
  print("\n\n")

  return dataframe

