#importing Pandas
import pandas as pd

#read data file
melbourne_file_path= "../data/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)

#print columns
print(melbourne_data.columns)

melbourne_data=melbourne_data.dropna(axis=0)

print(melbourne_data.columns)

#store a clumn in variable
#y=melbourne_data.Price
#print(y)

#Features data
melbourne_features=["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]
X=melbourne_data[melbourne_features]
print(X.columns)

print(X.describe())