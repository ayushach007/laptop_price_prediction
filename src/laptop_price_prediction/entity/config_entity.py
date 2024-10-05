from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataIngestionConfig:
    raw_path: Path
    train_path: Path
    test_path: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    preprocessor_path: Path
    train_arr_path: Path
    test_arr_path: Path


@dataclass(frozen=True)
class ModelBuildingConfig:
    model_path: Path
    train_metrics_path: Path
    test_metrics_path: Path