from src.preprocess import load_iris_dataset, convert_species_to_int

def main():
    df = load_iris_dataset()
    df = convert_species_to_int(df)
    
    print("Primeiras linhas do dataset:")
    print(df.head())

if __name__ == "__main__":
    main()
