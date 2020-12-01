import logging

FORMAT = logging.Formatter(
    "%(asctime)s - %(levelname)s : %(filename)s - %(funcName)s : %(message)s")


def DevelopmentLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs/development.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(FORMAT)

    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    stream_handler.setFormatter(FORMAT)

    logger.addHandler(stream_handler)

    return logger


def TestingLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs/testing.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(FORMAT)

    logger.addHandler(file_handler)

    return logger


def ProductionLogger():
    import google.cloud.logging
    from google.cloud.logging.handlers import CloudLoggingHandler

    client = google.cloud.logging.Client()
    handler = CloudLoggingHandler(client)

    cloud_logger = logging.getLogger('cloudLogger')
    cloud_logger.setLevel(logging.INFO)
    cloud_logger.addHandler(handler)

    return cloud_logger


logger = {
    "development": DevelopmentLogger,
    "testing": TestingLogger,
    "production": ProductionLogger,
    "default": ProductionLogger,
}
