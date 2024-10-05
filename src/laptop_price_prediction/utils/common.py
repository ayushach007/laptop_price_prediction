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
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import json
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
def load_object(file_path):
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
def save_transformed_data(data, file_path):
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
        data = pd.DataFrame(data)
        data.to_csv(file_path, index=False)
        logging.info('Transformed data saved successfully')

    except Exception as e:
        logging.error(f'Error saving transformed data to file: {e}')
        raise e



@ensure_annotations
def model_building_and_evaluation(X_train, y_train, X_test, y_test) -> dict:
    '''
    Build and evaluate a model

    Args:
        - X_train (np.array): Training data
        - y_train (np.array): Training labels
        - X_test (np.array): Testing data
        - y_test (np.array): Testing labels
        - model (object): Model to build and evaluate

    Returns:
        - dict: Model evaluation results
        - model: Model object
    '''
    try:
        logging.info('Building and evaluating model')
        model = GradientBoostingRegressor()

        logging.info('Turning hyperparameters')
        param_grid = {
            'n_estimators': [10, 50, 100, 200, 400, 450, 500],
            'max_depth': [3, 5, 7, 9, 11],
            'learning_rate': [1e-2, 1e-1, 1]
        }

        logging.info('Performing grid search')
        grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
        grid_search.fit(X_train, y_train)

        logging.info('Evaluating model')
        model = model.set_params(**grid_search.best_params_)
        model.fit(X_train, y_train)

        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        train_r2 = r2_score(y_train, y_pred_train)
        train_mse = mean_squared_error(y_train, y_pred_train)
        train_mae = mean_absolute_error(y_train, y_pred_train)

        test_r2 = r2_score(y_test, y_pred_test)
        test_mse = mean_squared_error(y_test, y_pred_test)
        test_mae = mean_absolute_error(y_test, y_pred_test)

        # save the train metrics and test metrics separately
        results = {
            'model': model,
            'train': {
                'r2': train_r2,
                'mse': train_mse,
                'mae': train_mae,
                'params': grid_search.best_params_
            },
            'test': {
                'r2': test_r2,
                'mse': test_mse,
                'mae': test_mae,
                'params': grid_search.best_params_
            }
        }

        logging.info('Model built and evaluated successfully')
        return results
    
    except Exception as e:
        logging.error(f'Error building and evaluating model: {e}')
        raise e
    

@ensure_annotations
def save_json(data, file_path):
    '''
    Save data to a JSON file

    Args:
        - data (dict): Data to save
        - file_path (str): Path to the file

    Raises:
        - Error: If there is an error saving the data
    '''
    try:
        logging.info('Saving data to JSON file')
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4, separators=(',', ': '))
        logging.info('Data saved to JSON file successfully')

    except Exception as e:
        logging.error(f'Error saving data to JSON file: {e}')
        raise e


