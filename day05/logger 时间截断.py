#Authon Ivor
import logging
from logging import handlers
import time

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

th = handlers.TimedRotatingFileHandler("access.log",when='S',interval=3,backupCount=3,encoding='utf-8')
th_formatter = logging.Formatter("%(asctime)s  %(levelno)s  %(name)s %(message)s")

th.setFormatter(th_formatter)

logger.addHandler(th)

logger.warning("This warning 1")
logger.warning("This warning 2")
time.sleep(5)
logger.warning("This warning 3")
logger.warning("This warning 4")