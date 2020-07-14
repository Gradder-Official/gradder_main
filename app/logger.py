import logging
import app.werkzeug_logger
from flask_login import current_user


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
class logger:

    @staticmethod
    def debug(message):
        from flask_login import current_user
        if current_user:
            file_handler = logging.FileHandler(f'./app/logs/{current_user.USERTYPE.lower()}_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - {} - {} - %(funcName)s - line %(lineno)d".format(current_user.email, current_user.USERTYPE)))
        else:
            file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
        log.addHandler(file_handler)
        log.debug(message)
    
    @staticmethod
    def info(message):
        from flask_login import current_user
        if current_user:
            file_handler = logging.FileHandler(f'./app/logs/{current_user.USERTYPE.lower()}_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - {} - {} - %(funcName)s - line %(lineno)d".format(current_user.email, current_user.USERTYPE)))
        else:
            file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
        log.addHandler(file_handler)
        log.info(message)
    
    @staticmethod
    def warning(message):
        from flask_login import current_user
        if current_user:
            file_handler = logging.FileHandler(f'./app/logs/{current_user.USERTYPE.lower()}_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - {} - {} - %(funcName)s - line %(lineno)d".format(current_user.email, current_user.USERTYPE)))
        else:
            file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
        log.addHandler(file_handler)
        log.warning(message)
    
    @staticmethod
    def critical(message):
        from flask_login import current_user
        if current_user:
            file_handler = logging.FileHandler(f'./app/logs/{current_user.USERTYPE.lower()}_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - {} - {} - %(funcName)s - line %(lineno)d".format(current_user.email, current_user.USERTYPE)))
        else:
            file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
        log.addHandler(file_handler)
        log.critical(message)

    @staticmethod
    def exception(message):
        from flask_login import current_user
        if current_user:
            file_handler = logging.FileHandler(f'./app/logs/{current_user.USERTYPE.lower()}_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - {} - {} - %(funcName)s - line %(lineno)d".format(current_user.email, current_user.USERTYPE)))
        else:
            file_handler = logging.FileHandler('./app/logs/user_actions.log', mode='a+')
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
        log.addHandler(file_handler)
        log.exception(message)