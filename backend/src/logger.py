"""Logger"""

import os
import logging
import sys

# Create logger instance
logger = logging.getLogger("task-manager-app")

env = os.getenv("ENV", "dev")
if env == "dev":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Avoid duplicate handlers
if not logger.handlers:
    logger.addHandler(console_handler)
