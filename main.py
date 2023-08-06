from WineQualityPrediction import logger
from WineQualityPrediction.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from WineQualityPrediction.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e
