import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import requests
from io import StringIO

#2.1 (a) Data Acquisiton
# Here we simulate a CSV download from a URL.
url = ""
response = requests.get(url)

#Check if the request was sucessful
if reponse.status_code == 200:
  print("Data sucessfully acquired!")
  data = pd.read_csv(StringIO(reponse.text))
else:
  print("Failed to aquire data.")
  data= None

# If data was sucessfully acquired, continue
if data is not None:
  print("Data Preview: ")
  print(data.head())

  # 2.1 (b) Data Cleaning
  # Handle missing values:
  # - Let's assume we drop rows with any missing target variables
  # - Impute missing values fro other features
  # - Remove duplicates if they exist

  # Drop rows with missing target variable (Let's assume the target is 'target_column')
  data = data.dropna(subset='target_column])

  # Impute missing values for other columns
  imputer = SimpleImputer(strategy='mean')  # Replace missing numeric values with the mean
  data_imputed = data.copy()
  data_imputed[data_imputed.columns] = imputer.fit_transform(data_imputed)

  # Remove duplicates
  data_imputed = data_imputed.drop_duplicates()

  # Preview cleaned data
  print("Cleaned Data Preview:")
  print(data_imputed.head())

  # 2.1 (c) Data Preprocessing
  # Preprocessing: We will apply scaling for numeric variables and one-hot encoding for categorical variables

  # Identify numeric and categorical columns
  numeric_cols = data_imputed.select_dtypes(include=['float64', 'int64']).columns
  categorical_cols = data_imputed.select_dtypes(include=['object']).columns

  # Define preprocessing steps for numeric and categorical features
  numeric_transformer = Pipeline(steps=[
  ('imputer', SimpleImputer(strategy='mean')),  # Impute missing values if any
  ('scaler', StandardScaler())  # Scale numeric features
    ])

  categorical_transformer = Pipeline(steps=[
  ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # Impute missing values
  ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))  # One-hot encode categorical features
    ])

  # Combine transformations for both numeric and categorical features using ColumnTransformer
  preprocessor = ColumnTransformer(
  transformers=[
  ('num', numeric_transformer, numeric_cols),
  ('cat', categorical_transformer, categorical_cols)
        ]
    )

  # Apply the preprocessing pipeline
  data_preprocessed = preprocessor.fit_transform(data_imputed)

  # Convert the preprocessed data back to a DataFrame
  # Get feature names after one-hot encoding
  categorical_columns_transformed = preprocessor.transformers_[1][1]['onehot'].get_feature_names_out(categorical_cols)
  all_feature_names = numeric_cols.tolist() + categorical_columns_transformed.tolist()

  data_preprocessed_df = pd.DataFrame(data_preprocessed, columns=all_feature_names)

  print("Preprocessed Data Preview:")
  print(data_preprocessed_df.head())

  # Save the preprocessed data to a new CSV file
  data_preprocessed_df.to_csv('preprocessed_data.csv', index=False)
  print("Preprocessed data saved to 'preprocessed_data.csv'.")
