from etl.extraction import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    # Caminhos
    input_path = 'dados/vendas_raw.csv'
    output_path = 'dados/'

    # Etapas ETL
    df = extract_data(input_path)
    df = transform_data(df)
    load_data(df, output_path)

if __name__ == "__main__":
    run_pipeline()

