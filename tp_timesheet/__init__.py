""" TP-Timesheet Module"""
import logging
from tp_timesheet.config import Config

__version__ = "0.4.0"

logger = logging.getLogger(__name__)
Config.ROOT_LOGGER = logger
