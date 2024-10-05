from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataIngestionConfig:
    raw_path: Path
    train_path: Path
    test_path: Path
