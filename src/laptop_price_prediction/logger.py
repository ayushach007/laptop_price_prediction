import os
import sys
import logging
from datetime import datetime

LOG_FILE_STYLES = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

# create log directory if it doesn't exist
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# specify log file path
log_file = os.path.join(log_dir, LOG_FILE_STYLES)

# create logger
logging.basicConfig(
    level=logging.INFO,
    format='[ %(asctime)s ] %(levelno)d %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)