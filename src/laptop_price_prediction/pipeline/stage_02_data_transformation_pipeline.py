from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.laptop_price_prediction.config.configurations import ConfigurationManager
from src.laptop_price_prediction.components.data_transformation import DataTransformation

class DataTransformationPipeline(DataIngestionPipeline):
    def __init__(self, train_path, test_path):
        self.train_path = train_path
        self.test_path = test_path

    def main(self):
        '''
        This function initiates the data transformation pipeline
        
        Returns:
            - Tuple[np.ndarray, np.ndarray]: Transformed train and test data

        Raises:
            - Error: If there is an error in the data transformation pipeline
        '''
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            train_arr, test_arr, _ =data_transformation.initiate_data_transformation(train_data_path=self.train_path, test_data_path=self.test_path)

            return train_arr, test_arr
        
        except Exception as e:
            logging.error(f"Error in data transformation pipeline: {e}")
            raise e
        