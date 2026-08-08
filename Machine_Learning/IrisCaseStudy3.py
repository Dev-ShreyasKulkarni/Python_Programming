from sklearn.datasets import load_iris

def main():
    print("-"*40)
    print("IRIS classification case study")
    print("-"*40)
    
    Dataset = load_iris()
    
    # Metadata of the dataset
    print("Independent Variables are: ")
    print(Dataset.feature_names)
    print("Length of Independent Variables :",len(Dataset.feature_names))
    print("Dependent Variables are: ")
    print(Dataset.target_names)
    print("Length of Dependent Variables :",len(Dataset.target_names))

    
if __name__ == "__main__":
    main()