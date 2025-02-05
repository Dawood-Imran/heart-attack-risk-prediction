from mlProject.components.data_validation import DataValiadtion
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME = "Data Validation"

class DataValidation_Training_Pipeline:
    
    def __init__(self):
        self.logger = logger

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e