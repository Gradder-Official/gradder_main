from datetime import datetime
from datetime import timedelta

from api import root_logger as logger
from google.cloud import storage


def upload_blob(filename: str, file_obj):
    storage_client = storage.Client()
    bucket = storage_client.bucket("gradder-storage")
    blob = bucket.blob(filename)
    blob.upload_from_file(file_obj, content_type=file_obj.content_type)

    logger.info(f"File {filename} uploaded")

    return blob


def download_blob(filename, actual_filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket("gradder-storage")
    blob = bucket.blob(filename)
    blob.download_to_filename(actual_filename)

    logger.info(f"File {actual_filename} - {filename}  downloaded")


def get_signed_url(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("gradder-storage")
    blob = bucket.get_blob(filename)

    logger.info(f"File {filename} opened from assignment")

    return blob.generate_signed_url(
        expiration=datetime.utcnow() + timedelta(seconds=3600)
    )
