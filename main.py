import logging
from src.laptop_price_prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.laptop_price_prediction.pipeline.stage_02_data_transformation_pipeline import DataTransformationPipeline
from src.laptop_price_prediction.pipeline.stage_03_model_building_pipeline import ModelBuildingPipeline

STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":
    try:
        logging.info(f"Initiating {STAGE_NAME} Pipeline")
        train_data_path, test_data_path = DataIngestionPipeline().main()
        logging.info(f"{STAGE_NAME} Pipeline completed successfully")
    
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME} Pipeline: {e}")
        raise e
    

STAGE_NAME = "Data Transformation"

if __name__ == "__main__":
    try:
        logging.info(f"Initiating {STAGE_NAME} Pipeline")
        train_arr, test_arr = DataTransformationPipeline(train_data_path, test_data_path).main()
        logging.info(f"{STAGE_NAME} Pipeline completed successfully")        
    
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME} Pipeline: {e}")
        raise e
    

STAGE_NAME = "Model Building"

if __name__ == "__main__":
    try:
        logging.info(f"Initiating {STAGE_NAME} Pipeline")
        ModelBuildingPipeline(train_arr, test_arr).main()
        logging.info(f"{STAGE_NAME} Pipeline completed successfully")
    
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME} Pipeline: {e}")
        raise e