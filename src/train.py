from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from src.preprocess import load_iris_dataset, convert_species_to_int
from pathlib import Path
import joblib

def train_decision_tree(save_model_path: Path = Path("models/decision_tree_model.joblib")):
    # Carregar e preparar dados
    df = load_iris_dataset()
    df = convert_species_to_int(df)

    X = df.drop("species", axis=1)
    y = df["species"]

    # Particionar em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Instanciar e treinar
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Avaliar
    y_pred = clf.predict(X_test)
    print("Accuracy on test set:", accuracy_score(y_test, y_pred))
    print("Classification report:\n", classification_report(y_test, y_pred))

    # Salvar o modelo treinado
    save_model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, save_model_path)
    print(f"Modelo salvo em: {save_model_path}")

    return clf, X_test, y_test, y_pred
