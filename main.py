from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationPipeline

STAGE_NAME="Data Ingestion stage"

try:
    
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========")
        
except Exception as e:     
        logger.exception(e)
        raise e


STAGE_NAME="Data Validation stage"

try:
    
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========")
        
except Exception as e:     
        logger.exception(e)
        raise e


from src.mlproject.config.configuration import ConfigurationManager2
from src.mlproject.components.DataTransformation import DataTransformation

STAGE_NAME="Data Transformation stage"

try:
    
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        data_validation = DataTransformationPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========")
        
except Exception as e:     
        logger.exception(e)
        raise e

from src.mlproject.config.configuration import ConfigurationManager3
from src.mlproject.components.Model_trainer import ModelTrainer
from src.mlproject.pipeline.stage_04_model_training import ModelTrainingPipeline


STAGE_NAME="Model Training stage"

try:
    
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        data_validation = ModelTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========")
        
except Exception as e:     
        logger.exception(e)
        raise e


from src.mlproject.config.configuration import ConfigurationManager4
from src.mlproject.components.Model_Evaluation import ModelEvaluation
from src.mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME="Model Evaluation stage"

try:
    
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        data_validation = ModelEvaluationPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========")
        
except Exception as e:     
        logger.exception(e)
        raise e