
import os
import sys
import logging
from datetime import datetime
from from_root import from_root

log_path = os.path.join(from_root(), 'log', f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")
os.makedirs(log_path, exist_ok=True)

log_filepath = os.path.join(log_path, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("mlProjectLogger")
