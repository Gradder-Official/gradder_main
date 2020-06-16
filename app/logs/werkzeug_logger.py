import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
log.addHandler(stream_handler)
log.removeHandler(logging.FileHandler)