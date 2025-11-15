import numpy as np
from pathlib import Path
import joblib

def predict_species(model_path: Path, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> int:
    """Carrega o modelo salvo e faz a predição da espécie (retorna 1,2 ou 3)."""
    clf = joblib.load(model_path)
    X_new = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = clf.predict(X_new)
    return int(pred[0])
