from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir : Path

@dataclass(frozen=True)
class DataValidataionConfig:
    root_dir : Path
    STATUS_FILE : str
    unzip_data_dir : Path
    all_schema : dict


from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)

class DataTransformationConfig:
    root_dir: Path
    data_path : Path
    

from pathlib import Path
from dataclasses import dataclass
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    train_data_path : Path
    test_data_path : Path
    model_name : str
    alpha : float
    l1_ratio : float
    target_column : str

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)

class ModelEvaluationConfig:
    root_dir : Path
    test_data_path : Path
    model_path : Path
    all_params : dict
    metric_file_name : Path
    target_column : str
    mlflow_uri : str