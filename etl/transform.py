# 2. Transformação (T)
def transform_data(df):
    # Padronizar a coluna de data (YYYY-MM-DD). (Alessa)
    # Padronizar coluna de data
    df['data'] = pd.to_datetime(df['data'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    # Verificar o resultado
    print(df['data'].head())

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

    # Remover ou corrigir preços negativos.
    if 'preco_unitario' in dataframe.columns:
        dataframe = dataframe[dataframe['preco_unitario'] >= 0]

    # Criar uma nova coluna valor_total = quantidade * preco_unitario.
    if 'quantidade' in df.columns and 'preco_unitario' in dataframe.columns:
        dataframe['valor_total'] = dataframe['quantidade'] * dataframe['preco_unitario']
