import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# initialise the Data Ingestion Configuration 

@dataclass #with this insteadt of __init__ we can use the classes
class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

# Crete a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method Starts')
        try:
            #df = pd.read_csv('notebooks/data/gemstone.csv')   #csv path or use
            df = pd.read_csv(os.path.join('notebooks/data','gemstone.csv') ) 
            logging.info('dataset read as pandas dataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) # make directory
            df.to_csv(self.ingestion_config.raw_data_path,index=False) # save csv file
            logging.info('Train Test split')

            train_set,test_set =train_test_split(df,test_size=0.3,random_state=42) #split data into train test

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=False)  #saving train set data
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=False)  # saving test set data
            logging.info('Ingestion of Data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info('Exception Occured in Data Ingestion stage')
            raise CustomException(e,sys)
        

## run data ingestion

if __name__=='__main__':
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion() #get both the paths