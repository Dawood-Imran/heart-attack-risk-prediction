
from mlProject.components.data_ingestion import DataIngestion
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger

STAGE_NAME = "Data Ingestion"

class DataIngestion_Training_Pipeline:

    def __init__(self):
        self.logger = logger

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e