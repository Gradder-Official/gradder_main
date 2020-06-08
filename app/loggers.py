import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
logger.addHandler(file_handler)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
log.addHandler(stream_handler)
log.removeHandler(logging.FileHandler)