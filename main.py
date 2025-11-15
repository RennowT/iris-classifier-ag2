from src.train import train_decision_tree
from src.predict import predict_species
from pathlib import Path

def main():
    # Treinar o modelo
    clf, X_test, y_test, y_pred = train_decision_tree()

    # Exemplo de predição com novos dados
    model_path = Path("models/decision_tree_model.joblib")
    result = predict_species(model_path, 5.1, 3.5, 1.4, 0.2)
    print("Predicted species (int):", result)

if __name__ == "__main__":
    main()
