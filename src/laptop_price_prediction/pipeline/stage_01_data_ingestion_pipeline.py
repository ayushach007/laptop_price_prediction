from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.config.configurations import ConfigurationManager
from src.laptop_price_prediction.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self, config):
        self.config = config

    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            return train_path, test_path
        except Exception as e:
            logging.error(f"Error in data ingestion pipeline: {e}")
            raise e
        

STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try:
        logging.info(f"Initiating {STAGE_NAME} Pipeline")
        DataIngestionPipeline(config=None).main()
        logging.info(f"{STAGE_NAME} Pipeline completed successfully")
    
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME} Pipeline: {e}")
        raise e

