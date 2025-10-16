# 2. Transformação (T)

# Padronizar a coluna de data (YYYY-MM-DD). (Alessa)

# Substituir valores nulos por "Não informado". (Dani)

import pandas as pd

dataframe = pd.read_csv('vendas.csv')

newDataframe = dataframe.fillna('Não Informado')

print(newDataframe.to_string())

# Corrigir quantidade para ser sempre um número inteiro. (Vitória)

dataframe['quantidade'].unique()

dataframe['quantidade'] = dataframe['quantidade'].replace('três', '3')

dataframe['quantidade'] = pd.to_numeric(dataframe['quantidade'])
dataframe.dtypes

# Remover ou corrigir preços negativos. (Nicoli)


# Criar uma nova coluna valor_total = quantidade * preco_unitario. ()

