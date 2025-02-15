from mlProject.config.configuration import DataTransformationConfig
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import os
from mlProject import logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
        """
        Performs data transformations, including encoding categorical features,
        scaling numerical features, and splitting the data.
        """
        data = pd.read_csv(self.config.data_path)
        print(data.shape)
        print(data['Heart_Attack_Risk'].value_counts())
        colmns = self.config.all_schema

        # Convert columns to specified data types
        for column, dtype in colmns.items():
            try:
                data[column] = data[column].astype(dtype)
            except ValueError as e:
                logger.warning(f"Error converting column '{column}' to type '{dtype}': {e}")

        # Define categorical and numerical columns
        cat_cols = ["Smoking", "Alcohol_Consumption", "Diabetes", "Hypertension", 
                    "Family_History", "Fasting_Blood_Sugar", "Exercise_Induced_Angina",
                    "Physical_Activity_Level", "Gender", "Stress_Level", 
                    "Chest_Pain_Type", "Thalassemia", "ECG_Results"]  # Include all categorical columns
        num_cols = [col for col in data.columns if col not in cat_cols and col != 'Heart_Attack_Risk']

        # One-Hot Encoding for Categorical Columns
        # Create a OneHotEncoder object
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore', drop='first') # Set sparse=False for dense output
        encoded_data = encoder.fit_transform(data[cat_cols])
        encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(cat_cols))
        data = data.drop(columns=cat_cols)
        data = pd.concat([data, encoded_df], axis=1)

        # Label Encoding for Target Variable
        label_encoder = LabelEncoder()
        label_encoder.fit(data['Heart_Attack_Risk'])
        print(label_encoder.classes_)
        print(label_encoder.transform(label_encoder.classes_))
        data['Heart_Attack_Risk_Encoded'] = label_encoder.transform(data['Heart_Attack_Risk'])
        data.drop('Heart_Attack_Risk', axis=1, inplace=True)

        # Scaling Numerical Features
        scaler = StandardScaler()
        data[num_cols] = scaler.fit_transform(data[num_cols])

        
        smote = SMOTE(random_state=42)
        X = data.drop('Heart_Attack_Risk_Encoded', axis=1)
        y = data['Heart_Attack_Risk_Encoded']
        X_resampled, y_resampled = smote.fit_resample(X, y)

        # Combine resampled data
        data_resampled = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.DataFrame(y_resampled, columns=['Heart_Attack_Risk_Encoded'])], axis=1)
        print(data_resampled['Heart_Attack_Risk_Encoded'].value_counts())

        # Split the data into training and test sets
        train, test = train_test_split(data_resampled, test_size=0.25, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data transformation, handling imbalanced data, and splitting completed.")
        logger.info(f"Train data shape: {train.shape}")

        print(train.shape)
        print(test.shape)
        print(data) 