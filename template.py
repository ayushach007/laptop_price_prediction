import logging 
import os
from pathlib import Path
logging.info('Started to create directories')

project_name = 'laptop_price_prediction'

files = [
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_building_and_evaluation.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/stage_01_data_ingestion_pipeline.py',
    f'src/{project_name}/pipeline/stage_02_data_transformation_pipeline.py',
    f'src/{project_name}/pipeline/stage_03_model_building_pipeline.py',
    f'src/{project_name}/pipeline/stage_04_prediction_pipeline.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/constants/constant.py',
    'notebook/data_ingestion.ipynb',
    'notebook/data_transformation.ipynb',
    'notebook/model_building.ipynb',
    'notebook/prediction.ipynb',
    'notebook/EDA.ipynb',
    'notebook/model_training.ipynb',
    'config/config.yaml',
    'requirements.txt',
    'setup.py',
    'Dockerfile',
    'main.py',
    'app.py'
]


def create_files():
    '''
    This function creates all the files and directories specified in the files list
    '''
    for file in files:
        file = Path(file)
        file_dir, file_name = os.path.split(file)

        if file_dir != '':
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f'{file_dir} created for {file_name}')

        try:
            if not os.path.exists(file) or os.path.getsize(file) == 0:
                with open(file, 'w') as f:
                    # File is intentionally left empty
                    f.write('')
            else:
                logging.info(f'{file} already exists')

            logging.info(f'{file} created')
        except PermissionError as e:
            logging.error(f'Permission denied: {file} - {e}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    create_files()
    logging.info('All files created successfully')