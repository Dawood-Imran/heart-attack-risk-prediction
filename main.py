from mlProject.pipeline.stage_01_data_ingestion  import DataIngestion_Training_Pipeline
from mlProject.pipeline.stage_02_data_validation import DataValidation_Training_Pipeline
from mlProject import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestion_Training_Pipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f"stage {STAGE_NAME} failed! Error: {str(e)}")
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidation_Training_Pipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f"stage {STAGE_NAME} failed! Error: {str(e)}")
    raise e
