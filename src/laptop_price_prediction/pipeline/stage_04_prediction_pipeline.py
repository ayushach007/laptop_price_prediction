import pandas as pd
from src.laptop_price_prediction.logger import logging
from src.laptop_price_prediction.utils.common import load_object

class Prediction():
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            logging.info('Loading preprocessing pipeline')
            preprocessor = load_object('artifacts/data_transformation/preprocessor.pkl')
            logging.info('Successfully loaded preprocessing pipeline')

            logging.info('Loading model')
            model = load_object('artifacts/model/model.pkl')
            logging.info('Successfully loaded model')

            logging.info('Preprocessing input features')
            features = preprocessor.transform(features)
            logging.info('Successfully preprocessed input features')

            logging.info('Predicting price')
            price = model.predict(features)
            logging.info('Successfully predicted price')

            return price
        
        except Exception as e:
            logging.error(f'Error occured while predicting price: {e}')
            return None


class CustomData():
    def __init__(self,
                 Company: str,
                 Product: str,
                 Type_Name: str,
                 Inched: float,
                 ScreenResolution: str,
                 Cpu: str,
                 Ram: int,
                 Memory: str,
                 Gpu: str,
                 OpSys: str,
                 Weight: float):

        try:
            logging.info('Creating custom data object')

            self.Company = Company
            self.Product = Product
            self.Type_Name = Type_Name
            self.Inched = Inched
            self.ScreenResolution = ScreenResolution
            self.Cpu = Cpu
            self.Ram = Ram
            self.Memory = Memory
            self.Gpu = Gpu
            self.OpSys = OpSys
            self.Weight = Weight

            logging.info('Successfully created custom data object')

        except Exception as e:
            logging.error(f'Error occured while creating custom data object: {e}')
            return None
        

    
    def get_data_as_dataframe(self):
        try:
            logging.info('Creating dataframe from custom data')
            data = {
                'Company': [self.Company],
                'Product': [self.Product],
                'TypeName': [self.Type_Name],
                'Inches': [self.Inched],
                'ScreenResolution': [self.ScreenResolution],
                'Cpu': [self.Cpu],
                'Ram': [self.Ram],
                'Memory': [self.Memory],
                'Gpu': [self.Gpu],
                'OpSys': [self.OpSys],
                'Weight': [self.Weight]
            }

            logging.info('Successfully created dataframe from custom data')

            return pd.DataFrame(data)
        
        except Exception as e:
            logging.error(f'Error occured while creating dataframe from custom data: {e}')
            return None