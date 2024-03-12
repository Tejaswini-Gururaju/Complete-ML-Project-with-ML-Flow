from src.mlproject.config.configuration import ConfigurationManager4
from src.mlproject.components.Model_Evaluation import ModelEvaluation
from src.mlproject import logger


STAGE_NAME="Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager4()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        logger.info("starting the logging to ML Flow")
        model_eval.log_into_mlflow()
        logger.info(" ML Flak task completed")

if __name__=="__main__":
     try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")

     except Exception as e:
          logger.exception(e)
          raise e