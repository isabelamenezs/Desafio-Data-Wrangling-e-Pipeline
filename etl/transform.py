--2. Transformação (T)

---Padronizar a coluna de data para o formato YYYY-MM-DD. (Alessa)

---Substituir valores nulos por "Não informado". (Dani)

import pandas as pd

dataframe = pd.read_csv('vendas.csv')

newDataframe = dataframe.fillna('Não Informado')

print(newDataframe.to_string())

---Corrigir a quantidade para ser sempre um número inteiro. (Vitoria)

---Remover ou corrigir preços negativos. (Nicoli)

