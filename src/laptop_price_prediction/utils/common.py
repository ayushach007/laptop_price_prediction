import os
import pandas as pd
import numpy as np
import logging
import pickle
import yaml
from pathlib import Path
from box import ConfigBox
import mysql.connector as mysql
from dotenv import load_dotenv
from ensure import ensure_annotations
from box.exceptions import BoxValueError
load_dotenv()


@ensure_annotations
def read_sql() -> pd.DataFrame:
    '''
    Read SQL queries from a file

    Returns:
        - pd.DataFrame: Data read from the SQL file

    Raises:
        - Error: If there is an error reading the data
    ''' 
    try:
        logging.info('Creating connection to MySQL database')
        conn = mysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=os.getenv('database')
        )

        logging.info('Reading data from MySQL database')
        # read the sql
        df = pd.read_sql_query('SELECT * FROM laptop', conn)
        logging.info('Data read successfully')
        return df

    except Exception as e:
        logging.error(f'Error reading data from MySQL database: {e}')
        raise e



@ensure_annotations
def read_yaml(yamal_file_path: Path) -> ConfigBox:
    '''
    Read YAML file

    Args:
        - file_path (str): Path to the YAML file

    Returns:
        - dict: Data read from the YAML file

    Raises:
        - Error: If there is an error reading the data
    '''
    try:
        with open(yamal_file_path, 'r') as file:
            content =  yaml.safe_load(file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def save_object(obj, file_path):
    '''
    Save object to a file

    Args:
        - obj (object): Object to save
        - file_path (str): Path to the file

    Raises:
        - Error: If there is an error saving the object
    '''
    try:
        logging.info('Saving object to file')
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info('Object saved successfully')

    except Exception as e:
        logging.error(f'Error saving object to file: {e}')
        raise e
    

@ensure_annotations
def load_object(file_path: Path):
    '''
    Load object from a file

    Args:
        - file_path (str): Path to the file

    Returns:
        - object: Object loaded from the file

    Raises:
        - Error: If there is an error loading the object
    '''
    try:
        logging.info('Loading object from file')
        with open(file_path, 'rb') as file:
            obj = pickle.load(file)
        logging.info('Object loaded successfully')
        return obj

    except Exception as e:
        logging.error(f'Error loading object from file: {e}')
        raise e
    
@ensure_annotations
def create_directories(dirs: list):
    '''
    Create directories if they don't exist

    Args:
        - dirs (list): List of directories to create
    '''
    try:
        logging.info('Creating directories')
        for dir in dirs:
            os.makedirs(dir, exist_ok=True)
        logging.info('Directories created successfully')

    except Exception as e:
        logging.error(f'Error creating directories: {e}')
        raise e
    

@ensure_annotations
def save_transformed_data(data: np.array, file_path: Path):
    '''
    Save transformed data to a file

    Args:
        - data (np.array): Data to save
        - file_path (str): Path to the file

    Raises:
        - Error: If there is an error saving the data
    '''
    try:
        logging.info('Saving transformed data to file')
        data.to_csv(file_path, index=False)
        logging.info('Transformed data saved successfully')

    except Exception as e:
        logging.error(f'Error saving transformed data to file: {e}')
        raise e


