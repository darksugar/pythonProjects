#Authon Ivor
import logging

#创建一个logger
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

log_file = "access.log"

#创建屏幕输出
console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.INFO)

#创建文件输出
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(level=logging.ERROR)

#创建格式化输出
ch_formatter = logging.Formatter("%(asctime)s  %(levelno)s  %(name)s %(message)s")
fh_formatter = logging.Formatter("%(asctime)s  %(levelno)s  %(name)s %(message)s")

#将输出格式添加到handler
console_handler.setFormatter(ch_formatter)
file_handler.setFormatter(fh_formatter)

#将handler添加到logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#日志输出测试
logger.info("This is info")
logger.error("This is error")