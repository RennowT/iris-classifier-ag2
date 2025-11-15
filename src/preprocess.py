import pandas as pd
from pathlib import Path


def load_iris_dataset():
    """Carrega o conjunto de dados iris.csv da pasta data/."""
    data_path = Path("data/iris.csv")

    if not data_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {data_path}")

    df = pd.read_csv(data_path)
    return df
