"""Logger"""

import logging
import sys

# Create logger instance
logger = logging.getLogger("task-manager-app")
logger.setLevel(logging.INFO)  # Change to DEBUG for more verbose output

# Create formatter
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Avoid duplicate handlers in hot-reloading
if not logger.handlers:
    logger.addHandler(console_handler)
