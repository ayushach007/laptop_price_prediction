from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.pipeline.stage_02_data_transformation_pipeline import DataTransformationPipeline
from src.laptop_price_prediction.config.configurations import ConfigurationManager
from src.laptop_price_prediction.components.model_building_and_evaluation import ModelBuilding 


class ModelBuildingPipeline(DataTransformationPipeline):
    def __init__(self, train_arr, test_arr):
        self.train_arr = train_arr
        self.test_arr = test_arr

    def main(self):
        '''
        This function initiates the model building pipeline
        
        Raises:
            - Error: If there is an error in the model building pipeline
        '''
        try:
            config = ConfigurationManager()
            model_building_config = config.get_model_building_config()
            model_building = ModelBuilding(model_building_config)
            model_building.initiate_model_building(train_arr=self.train_arr, test_arr=self.test_arr)
        
        except Exception as e:
            logging.error(f"Error in Model Building Pipeline: {e}")
            raise e
        

