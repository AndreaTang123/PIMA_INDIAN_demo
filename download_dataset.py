import kagglehub
from kagglehub import KaggleDatasetAdapter
dataset_name = "uciml/pima-indians-diabetes-database"
file_path = "diabetes.csv"
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    dataset_name,
    file_path
)
print("Success\n")
print("First 5 rows：")
print(df.head())

print("\dataset information：")
print(df.info())

print("\ndescriptive statistics：")
print(df.describe())