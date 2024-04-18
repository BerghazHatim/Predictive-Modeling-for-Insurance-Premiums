import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging
from utils import save_object

@dataclass
class DataTransfomationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransfomationConfig()

    def get_data_transformer_object(self):
        '''
        Description: this function is responsable for data pipeline
        '''
        try:

            numerical_columns = [
                "age",
                "bmi",
                "children"
                ]
            categorical_columns = [
                "sex",
                "smoker",
                "region"
                ]
            
            num_pipeline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )
            logging.info("numerical columns scaler completed successfully")

            cat_pipeline = Pipeline(
                
                steps=[
                    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("categorical columns encoding and scaler completed successfully")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", num_pipeline, numerical_columns),
                    ("categorical_pipeline", cat_pipeline, categorical_columns),        
            ]
            )

            logging.info("Column transformation completed successfully")
            return preprocessor
        
        except CustomException as error:
            raise CustomException(error,sys)   
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data done.")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "charges"

            X_train_df = train_df.drop(columns=[target_column_name],axis=1)
            y_train_df = train_df[target_column_name]

            X_test_df = test_df.drop(columns=[target_column_name],axis=1)
            y_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing transformation on features and targets")

            X_train_transformed_array = preprocessing_obj.fit_transform(X_train_df)
            X_test_transformed_array = preprocessing_obj.transform(X_test_df)
            logging.info(f"Applying preprocessing transformation on features and targets completed successfully")

            train_array = np.c_[X_train_transformed_array, np.array(y_train_df)]
            test_array = np.c_[X_test_transformed_array, np.array(y_test_df)]
            logging.info("features and targets concatenated succssefully")

            save_object(

                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj

            )

            return(
                train_array,test_array,self.data_transformation_config.preprocessor_obj_file_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)