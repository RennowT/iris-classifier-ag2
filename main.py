from src.preprocess import load_iris_dataset

def main():
    df = load_iris_dataset()
    print("Primeiras linhas do dataset:")
    print(df.head())

if __name__ == "__main__":
    main()
