import logging
import app.logs.werkzeug_logger

user_logger = logging.getLogger(__name__)
user_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
user_logger.addHandler(file_handler)