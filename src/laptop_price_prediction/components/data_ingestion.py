import pandas as pd
from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.utils.common import read_sql
from src.laptop_price_prediction.entity.config_entity import DataIngestionConfig
from typing import Tuple
from sklearn.model_selection import train_test_split



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        '''
        This function reads data from the SQL database, splits it into train and test data and saves it in the specified paths
        
        Returns:
            - Tuple[pd.DataFrame, pd.DataFrame]: Train and Test data
        '''
        
        try:
            df = read_sql()

            logging.info(f"Data loaded successfully")
            df.to_csv(self.config.raw_path, index=False, header=True)

            logging.info(f"Data saved successfully")

            logging.info(f"Splitting data into train and test data")
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            logging.info(f"Data split successfully")

            train_data.to_csv(self.config.train_path, index=False, header=True)
            test_data.to_csv(self.config.test_path, index=False, header=True)

            logging.info(f"Train and Test data saved successfully")

            return (
                self.config.train_path,
                self.config.test_path
            )
        
        except Exception as e:
            logging.error(f"Error in data ingestion: {e}")
            raise e
        