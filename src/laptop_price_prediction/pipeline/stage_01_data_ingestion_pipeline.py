from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.config.configurations import ConfigurationManager
from src.laptop_price_prediction.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        '''
        This function initiates the data ingestion pipeline

        Returns:
            - Tuple[pd.DataFrame, pd.DataFrame]: Paths to the train and test data

        Raises:
            - Error: If there is an error in the data ingestion pipeline
        '''
        try:
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            return train_path, test_path
        except Exception as e:
            logging.error(f"Error in data ingestion pipeline: {e}")
            raise e

