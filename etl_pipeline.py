import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def extract():
    df = pd.read_csv("Titanic-Dataset.csv")
    print("Data loaded:", df.shape)
    print(df.head())
    df = df.drop(columns=["Name", "Ticket", "Cabin", "PassengerId"])
    return df

def transform(df):
    X = df.drop(columns=["Survived"])
    num_cols = X.select_dtypes(include=["int64","float64"]).columns.tolist()
    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()

    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler",  StandardScaler()),
    ])
    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols),
    ])

    X_processed = preprocessor.fit_transform(X)
    print("Transformed shape:", X_processed.shape)
    return X_processed

def load(X_processed):
    df_out = pd.DataFrame(X_processed)
    df_out.to_csv("processed_data.csv", index=False)
    print("Saved to processed_data.csv")

if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)