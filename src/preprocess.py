import pandas as pd
from pathlib import Path


def load_iris_dataset():
    """Carrega o conjunto de dados iris.csv da pasta data/."""
    data_path = Path("data/iris.csv")

    if not data_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {data_path}")

    df = pd.read_csv(data_path)
    return df


def convert_species_to_int(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte a coluna 'species' de strings para inteiros
    conforme o mapeamento da AG2.
    """
    mapping = {
        "Iris-setosa": 1,
        "Iris-versicolor": 2,
        "Iris-virginica": 3
    }

    df["species"] = df["species"].replace(mapping).astype("int64")
    return df
