from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.utils.common import read_yaml, create_directories
from src.laptop_price_prediction.entity.config_entity import DataIngestionConfig
from src.laptop_price_prediction.entity.config_entity import DataTransformationConfig
from src.laptop_price_prediction.entity.config_entity import ModelBuildingConfig
from src.laptop_price_prediction.constants.constant import *


class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH):
        '''
        This class is used to load the configuration file and assign the paths to the raw, train and test data
        
        Args:
            config_file_path (Path): Path to the configuration file
        '''

        try:
            self.config = read_yaml(config_file_path)
            logging.info(f"Configuration file loaded successfully")

            logging.info(f'Creating directories to stor artifacts')
            create_directories([self.config.artifacts])
        
        except Exception as e:
            logging.error(f"Error loading configuration file: {e}")
            raise e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        '''
        This function loads the data ingestion configuration from the configuration file
        
        Returns:
            - DataIngestionConfig: Data Ingestion Configuration
        
        Raises:
            - Error: If there is an error loading the configuration
        '''

        try:
            config = self.config.data_ingestion
            logging.info(f"Data Ingestion Configuration loaded successfully")

            logging.info(f"Creating directories to store data")
            create_directories([config.root_dir])

            logging.info(f"Successfully created directories to store data")

            logging.info(f"Assigning paths to raw, train and test data")
            
            data_ingestion_config = DataIngestionConfig(
                raw_path = config.raw_path,
                train_path = config.train_path,
                test_path = config.test_path
            )

            logging.info(f"Paths assigned successfully")
            
            return data_ingestion_config
        
        except Exception as e:
            logging.error(f"Error loading data ingestion configuration: {e}")
            raise e
        

    def get_data_transformation_config(self) -> DataTransformationConfig:
        '''
        This function loads the data transformation configuration from the configuration file
        
        Returns:
            - DataTransformationConfig: Data Transformation Configuration
        
        Raises:
            - Error: If there is an error loading the configuration
        '''
        try:
            config = self.config.data_transformation
            logging.info(f"Data Transformation Configuration loaded successfully")

            logging.info(f"Creating directories to store transformed data and preprocessor")
            create_directories([config.root_dir])

            logging.info(f"Successfully created directories to store transformed data and preprocessor")

            logging.info(f"Assigning paths to transformed train and test data and preprocessor")
            
            data_ingestion_config = DataTransformationConfig(
                preprocessor_path=config.preprocessor_path,
                train_arr_path=config.train_arr_path,
                test_arr_path=config.test_arr_path
            )

            logging.info(f"Paths assigned successfully")
            
            return data_ingestion_config
        
        except Exception as e:
            logging.error(f"Error loading data ingestion configuration: {e}")
            raise e
        
    def get_model_building_config(self) -> ModelBuildingConfig:
        '''
        This function loads the model building configuration from the configuration file
        
        Returns:
            - ModelBuildingConfig: Model Building Configuration
            
        Raises:
            - Error: If there is an error loading the configuration
        '''
        try:
            config = self.config.model
            logging.info(f"Model Building Configuration loaded successfully")

            logging.info(f"Creating directories to store model and metrics")
            create_directories([config.root_dir])

            logging.info(f"Successfully created directories to store model and metrics")

            logging.info(f"Assigning paths to model and metrics")
            
            data_ingestion_config = ModelBuildingConfig(
                model_path=config.model_path,
                train_metrics_path=config.train_metrics_path,
                test_metrics_path=config.test_metrics_path
            )

            logging.info(f"Paths assigned successfully")
            
            return data_ingestion_config
        
        except Exception as e:
            logging.error(f"Error loading data ingestion configuration: {e}")
            raise e