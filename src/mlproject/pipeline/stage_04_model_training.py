from src.mlproject.config.configuration import ConfigurationManager3
from src.mlproject.components.Model_trainer import ModelTrainer
from src.mlproject import logger


STAGE_NAME="Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager3()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__=="__main__":
     try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")

     except Exception as e:
          logger.exception(e)
          raise e

