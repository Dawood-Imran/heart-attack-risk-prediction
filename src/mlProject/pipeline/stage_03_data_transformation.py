from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME = "Data Transformation"


class DataTransformation_Training_Pipeline:
    
    def __init__(self):
        self.logger = logger

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.transform_data()
        except Exception as e:
            raise e
