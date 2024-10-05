from src.laptop_price_prediction.utils.common import read_yaml, create_directories
from src.laptop_price_prediction.entity.config_entity import DataIngestionConfig
from src.laptop_price_prediction.components.data_ingestion import DataIngestion

from src.laptop_price_prediction.constants.constant import *
from src.laptop_price_prediction.logger import logging

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
        

if __name__ == "__main__":
    try:
        logging.info(f'Initiating Data Ingestion')
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
        logging.info(f'Data Ingestion completed successfully')
    except Exception as e:
        logging.error(f'Error: {e}')
        raise e