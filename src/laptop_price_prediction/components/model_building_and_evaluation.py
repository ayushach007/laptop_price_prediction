import pandas as pd
from pathlib import Path
from src.laptop_price_prediction.utils.common import save_object, save_json, model_building_and_evaluation
from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.entity.config_entity import ModelBuildingConfig

class ModelBuilding:
    def __init__(self, config: ModelBuildingConfig):
        self.config = config

    def initiate_model_building(self, train_arr, test_arr):
        '''
        This function reads the train and test data, splits the data into features and target, builds the model and saves the model and metrics
        
        Args:
            - train_arr (Path): Path to the transformed training data
            - test_arr (Path): Path to the transformed test data
            
        Raises:
            - Error: If there is an error reading the data or building the model
        '''
        try:
            

            logging.info(f"Data read successfully")

            logging.info(f"Splittinf the data for model building")
            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            logging.info(f"Successfully split the training data for model building")

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logging.info(f"Successfully split the test data for model building")

            logging.info(f"Initiating model building")

            results = model_building_and_evaluation(X_train, y_train, X_test, y_test)

            logging.info(f"Model building completed successfully")

            logging.info(f"Saving model to {self.config.model_path}")
            save_object(results['model'], self.config.model_path)

            # save the metrics
            logging.info(f"Saving train metrics to {self.config.train_metrics_path}")
            save_json(results['train'], self.config.train_metrics_path)

            logging.info(f"Saving test metrics to {self.config.test_metrics_path}")

            save_json(results['test'], self.config.test_metrics_path)

            logging.info(f"Model building completed successfully")

        except Exception as e:
            logging.error(f"Error building model: {e}")
            raise e
