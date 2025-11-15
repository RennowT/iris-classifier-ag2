import pandas as pd
from pathlib import Path
import joblib

SPECIES_MAP = {
    1: "setosa",
    2: "versicolor",
    3: "virginica",
}

def predict_species(model_path: Path, sepal_length: float, sepal_width: float,
                    petal_length: float, petal_width: float) -> str:
    """Carrega o modelo e retorna a espécie prevista como texto."""
    
    clf = joblib.load(model_path)

    # Criamos um DataFrame com nomes de colunas para evitar warnings
    X_new = pd.DataFrame([{
        "sepal_length_cm": sepal_length,
        "sepal_width_cm": sepal_width,
        "petal_length_cm": petal_length,
        "petal_width_cm": petal_width
    }])

    pred = clf.predict(X_new)
    pred_class = int(pred[0])

    return SPECIES_MAP[pred_class]
