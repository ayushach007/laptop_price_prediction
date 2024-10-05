import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.laptop_price_prediction.entity.config_entity import DataTransformationConfig
from src.laptop_price_prediction.utils.common import save_object, save_transformed_data
from pathlib import Path
from src.laptop_price_prediction.logger import logging


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def create_preprocessor(self) -> pd.DataFrame:
        '''
        Create a preprocessor to transform the data
        
        Returns:
            - pd.DataFrame: Preprocessor to transform the data

        Raises:
            - Error: If there is an error creating the preprocessor
        '''
        try:
            numeric_features = ['Inches', 'Ram', 'Weight']
            categorical_features = ['Company', 'Product', 'TypeName', 'ScreenResolution', 'Cpu', 'Memory', 'Gpu', 'OpSys']

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)),
                    ('scaler', StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', num_pipeline, numeric_features),
                    ('cat', cat_pipeline, categorical_features)
                ]
            )

            logging.info(f"Preprocessor created successfully")

            return preprocessor
        
        except Exception as e:
            logging.error(f"Error creating preprocessor: {e}")
            raise e
        
    
    def initiate_data_transformation(self, train_data, test_data):
        '''
        This function reads the train and test data, splits the data into features and target, transforms the data and saves the transformed data
        
        Args:
            - train_data: Path to the train data
            - test_data: Path to the test data
            
        Returns:
            - tuple: Transformed train and test data and preprocessor path

        Raises:
            - Error: If there is an error reading the data or transforming the data
        '''
        
        try:
            logging.info(f"Initiating data transformation")

            logging.info(f"Reading train and test data")
            train_data = pd.read_csv(train_data)
            test_data = pd.read_csv(test_data)

            logging.info(f"Data read successfully")

            logging.info(f"Creating preprocessor")
            preprocessor = self.create_preprocessor()

            logging.info(f"Converting 'Ram' and 'Weight' feature to numeric dtype")
            train_data['Ram'] = train_data['Ram'].replace('GB', '', regex=True).astype(int)
            test_data['Ram'] = test_data['Ram'].replace('GB', '', regex=True).astype(int)

            train_data['Weight'] = train_data['Weight'].replace('kg', '', regex=True).astype(float)
            test_data['Weight'] = test_data['Weight'].replace('kg', '', regex=True).astype(float)

            logging.info(f"Successfully converted 'Ram' and 'Weight' feature to numeric dtype")

            logging.info(f"Splittng data into features and target")

            target = ['Price_euros']

            train_features = train_data.drop(target, axis=1)
            train_target = train_data[target]

            test_features = test_data.drop(target, axis=1)
            test_target = test_data[target]

            logging.info(f"Data split successfully")

            logging.info(f"Transforming train and test data")
            train_features = preprocessor.fit_transform(train_features)
            logging.info(f"Train data transformed successfully")

            test_features = preprocessor.transform(test_features)
            logging.info(f"Test data transformed successfully")

            logging.info(f"Converting transformed data to numpy array")
            train_arr = np.c_[
                train_features,
                np.array(train_target)
            ]

            test_arr = np.c_[
                test_features,
                np.array(test_target)
            ]

            logging.info(f"Data transformed successfully")

            logging.info(f"Saving preprocessor")
            save_object(
                obj=preprocessor,
                file_path=self.config.preprocessor_path
            )

            logging.info(f"Preprocessor saved successfully")    

            logging.info(f"Saving transformed train and test data")
            save_transformed_data(
                data=train_arr,
                file_path=self.config.train_arr_path
            )

            save_transformed_data(
                data = test_arr,
                file_path = self.config.test_arr_path
            )

            logging.info(f"Transformed data saved successfully")

            return (
                train_arr,
                test_arr,
                self.config.preprocessor_path
            )
        
        except Exception as e:
            logging.error(f"Error transforming data: {e}")
            raise e
