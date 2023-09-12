import logging
from airflow import DAG
import sys
import os
from airflow.decorators import task,dag
from datetime import datetime
from src.exception import ApplicationException
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, ModelTrainerArtifact
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# Define your DAG's default arguments
default_args = {
    'owner': 'your_username',
    'start_date': datetime(2023, 9, 12),
    # You can configure other default arguments as needed
}

# Create an Airflow DAG
@dag(
    'your_pipeline_dag',  # Unique ID for your DAG
    default_args=default_args,
    description='Your Pipeline DAG description',
    schedule_interval=None,  # Set the schedule interval as needed
    catchup=False,  # Set this to False if you don't want to run past DAG runs
)

def train_pipeline():

    @ task
    def data_ingestion():
        data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig()))
        return data_ingestion.initiate_data_ingestion()

    data_ingestion_artifact=data_ingestion()


dag = train_pipeline()