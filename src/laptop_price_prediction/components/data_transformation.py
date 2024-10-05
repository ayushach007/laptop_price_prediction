import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.laptop_price_prediction.entity.config_entity import DataTransformationConfig
from src.laptop_price_prediction.utils.common import save_object
from pathlib import Path
from src.laptop_price_prediction.logger import logging


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def create_preprocessor(self) -> pd.DataFrame:
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
        
    
    def initiate_data_transformation(self, train_data_path: Path, test_data_path: Path) -> pd.DataFrame:
        
        try:
            logging.info(f"Initiating data transformation")

            logging.info(f"Reading train and test data")
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)

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
            np.save(self.config.train_arr_path, train_arr)
            np.save(self.config.test_arr_path, test_arr)

            return (
                train_arr,
                test_arr
            )
        
        except Exception as e:
            logging.error(f"Error transforming data: {e}")
            raise e
