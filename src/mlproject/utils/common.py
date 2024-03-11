import os
import yaml
from src.mlproject import logger
from ensure import ensure_annotations
import json
import joblib
from box import Configbox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> Configbox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file : {path_to_yaml} loaded successfully")
            return Configbox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directory:list, verbose=True):
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path:Path) -> Configbox:

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded from : {path}")
    return Configbox(content)


@ensure_annotations
def save_bin(data=Any, path=Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at path : {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:

    data=joblib.load(path)
    logger.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:    #size in KB
    size = (os.path.getsize((path)/1024))
    logger.info(f"size of the file is : {size} kb")
    return size
