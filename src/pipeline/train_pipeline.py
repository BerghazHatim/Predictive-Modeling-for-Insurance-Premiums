import sys
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from components.data_ingestion import DataIngestionConfig
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransfomationConfig
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainerConfig
from components.model_trainer import ModelTrainer
from exception import CustomException



class trainPipeline:
    def __init__(self):
        pass
    def training(self,new_features):
        try:

            df = pd.read_csv("notebook\data\insurance.csv")

            df.loc[len(df)] = new_features

            obj = DataIngestion()
            train_data,test_data = obj.initiate_data_ingestion()
        
            data_transformation = DataTransformation()
            train_array,test_array,_=data_transformation.initiate_data_transformation(train_data,test_data)

            model_trainer = ModelTrainer()
            model_trainer.initiate_model_trainer(train_array,test_array)
        except Exception as e:
            raise CustomException(e,sys)









        
    