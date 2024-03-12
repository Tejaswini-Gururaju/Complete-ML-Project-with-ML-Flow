from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.config.configuration import ConfigurationManager1
from src.mlproject.components.DataValidation import DataValidation
from src.mlproject import logger

STAGE_NAME="Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager1()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
        