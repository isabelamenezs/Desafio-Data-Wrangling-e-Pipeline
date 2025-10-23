# 2. Transformação (T)
def transform_data(dataframe):
    import pandas as pd

    print("-----------------TRANSFORMAÇÃO-------------------\n")

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

    print("Visualização das 10 primeiras linhas da coluna 'data_venda' após a padronização da data (YYYY-MM-DD): \n")
    print(dataframe['data_venda'].head(10).to_string())
    print("\n\n")


    # Substituir valores nulos por "Não informado". (Dani)
    dataframe = dataframe.fillna('Não Informado')
    dataframe['quantidade'] = dataframe['quantidade'].replace('três', '3')
    dataframe['quantidade'] = pd.to_numeric(dataframe['quantidade'])
    dataframe.dtypes

    print("Visualização de 15 linhas após substituir valores nulos por 'Não informado': \n")
    print(dataframe.sample(15).to_string())
    print("\n\n")


    # Remover ou corrigir preços negativos. (Nicoli)
    if 'preco_unitario' in dataframe.columns:
        dataframe = dataframe[dataframe['preco_unitario'] >= 0]


    # Criar uma nova coluna valor_total = quantidade * preco_unitario. (Nicoli)
    if 'quantidade' in dataframe.columns and 'preco_unitario' in dataframe.columns:
        dataframe['valor_total'] = dataframe['quantidade'] * dataframe['preco_unitario']


    print("Visualização de 15 linhas após corrigir os preços negativos e criar a coluna 'valor_total': \n")
    print(dataframe.sample(15).to_string())
    print("\n\n")

    return dataframe
