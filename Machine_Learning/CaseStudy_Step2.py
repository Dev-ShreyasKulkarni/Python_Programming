import pandas as pd

Border = '-'*40

##################################################
# Step 1 : : Load the dataset
##################################################

print(Border)
print("Step 1 : : Load the dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")

print("Initial entries from dataset are :")
print(df.head())


##################################################
# Step 2 : : Data Analysis (EDA)
##################################################

print(Border)
print("Step 2 : : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing values per column : ")
print(df.isnull().sum())

print("Class distribution of species : ")
print(df["species"].value_counts())

print("Statistical Report of Dataset : ")
print(df.describe())