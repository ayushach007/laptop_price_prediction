from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.laptop_price_prediction.config.configurations import ConfigurationManager
from src.laptop_price_prediction.components.data_transformation import DataTransformation

class DataTransformationPipeline(DataIngestionPipeline):
    def __init__(self, train_data_path, test_data_path):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            train_arr, test_arr =data_transformation.initiate_data_transformation(self.train_data_path, self.test_data_path)

            return train_arr, test_arr
        
        except Exception as e:
            logging.error(f"Error in data transformation pipeline: {e}")
            raise e
        
STAGE_NAME = "Data Transformation"

if __name__ == "__main__":
    try:
        logging.info(f"Initiating {STAGE_NAME} Pipeline")

        logging.info(f"Reading data from previous stage: 'Data Ingestion Pipeline' ")
        train_data_path, test_data_path = DataIngestionPipeline().main()

        logging.info(f"Data read successfully")

        train_arr, test_arr = DataTransformationPipeline(train_data_path, test_data_path).main()
        logging.info(f"{STAGE_NAME} Pipeline completed successfully")        
    
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME} Pipeline: {e}")
        raise e