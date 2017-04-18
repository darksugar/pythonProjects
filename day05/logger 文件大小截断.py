#Authon Ivor
import logging
from logging import handlers

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

#大小截断
fh = handlers.RotatingFileHandler(filename="access.log",maxBytes=10,backupCount=3)
#输出格式
fh_formatter = logging.Formatter("%(asctime)s  %(levelno)s  %(name)s %(message)s")
#将输出格式赋给fh
fh.setFormatter(fh_formatter)

logger.addHandler(fh)

logger.warning("This warning 1")
logger.warning("This warning 2")
logger.warning("This warning 3")
logger.warning("This warning 4")
logger.warning("This warning 5")
logger.warning("This warning 6")