from src.mlproject.constants import *
from box import ConfigBox
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.utils.common import read_yaml, create_directories


from pathlib import Path
class ConfigurationManager:
    def __init__(
            self,
            # config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(Path("config/config.yaml"))
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_configuration(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
from src.mlproject.entity.config_entity import DataValidataionConfig

class ConfigurationManager1:
    def __init__(
            self,

            # config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(Path("config/config.yaml"))
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_validation_config(self) -> DataValidataionConfig:
        config= self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidataionConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )

        return data_validation_config