import pandas as pd

# 2. Transformação (T)
def transform_data(filepath):

    dataframe = pd.read_csv(filepath)

    # Padronizar a coluna de data (YYYY-MM-DD). (Alessa)
    dataframe['data_venda'] = (
        dataframe['data_venda']
        .astype(str)
        .str.strip()
        .str.replace(r'[/\.]', '-', regex=True)
    )

    datas = pd.to_datetime(dataframe['data_venda'], errors='coerce', format='%Y-%m-%d')

    mask_nat = datas.isna()
    datas[mask_nat] = pd.to_datetime(dataframe.loc[mask_nat, 'data_venda'], errors='coerce', dayfirst=True)

    dataframe['data_venda'] = datas.dt.strftime('%Y-%m-%d')

    print(dataframe['data_venda'].head(20))

    # Substituir valores nulos por "Não informado". (Dani)
    newDataframe = dataframe.fillna('Não Informado')

    print(newDataframe.to_string())

    # Corrigir quantidade para ser sempre um número inteiro. (Vitória)

    dataframe['quantidade'].unique()

    dataframe['quantidade'] = dataframe['quantidade'].replace('três', '3')

    dataframe['quantidade'] = pd.to_numeric(dataframe['quantidade'])
    dataframe.dtypes

    # Remover ou corrigir preços negativos. (Nicoli)
    if 'preco_unitario' in dataframe.columns:
        dataframe = dataframe[dataframe['preco_unitario'] >= 0]

    # Criar uma nova coluna valor_total = quantidade * preco_unitario. (Nicoli)
    if 'quantidade' in df.columns and 'preco_unitario' in dataframe.columns:
        dataframe['valor_total'] = dataframe['quantidade'] * dataframe['preco_unitario']

    return dataframe
