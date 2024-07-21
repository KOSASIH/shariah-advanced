import pandas as pd

def preprocess_data(data):
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    # Encode categorical variables
    data = pd.get_dummies(data, columns=['category'])
    return data
