import logging
import app.logs.werkzeug_logger

form_logger = logging.getLogger(__name__)
form_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('./app/logs/forms.log', mode='a+')
form_logger.addHandler(file_handler)

