from pathlib import Path
from src.train import train_decision_tree
from src.predict import predict_species

def ask_user_for_inputs():
    print("\n=== Classificação de nova amostra ===")
    sepal_length = float(input("Comprimento da sépala (cm): "))
    sepal_width  = float(input("Largura da sépala (cm): "))
    petal_length = float(input("Comprimento da pétala (cm): "))
    petal_width  = float(input("Largura da pétala (cm): "))
    return sepal_length, sepal_width, petal_length, petal_width


def main():
    train_decision_tree()

    values = ask_user_for_inputs()
    
    model_path = Path("models/decision_tree_model.joblib")
    species = predict_species(model_path, *values)

    print(f"\n>>> A espécie prevista é: {species}.\n")


if __name__ == "__main__":
    main()
