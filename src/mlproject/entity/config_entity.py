from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir : Path

@dataclass
class DataValidataionConfig:
    root_dir : Path
    STATUS_FILE : str
    unzip_data_dir : Path
    all_schema : dict
