import os
from google.cloud import storage
from app.logs.form_logger import form_logger
from datetime import datetime, timedelta

def upload_blob(filename:str, file_obj):
    storage_client = storage.Client()
    bucket = storage_client.bucket('gradder-storage')
    blob = bucket.blob(filename)
    blob.upload_from_file(file_obj, content_type=file_obj.content_type)
    form_logger.info('File {} uploaded'.format(filename))
    return blob
    
def download_blob(filename, actual_filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket('gradder-storage')
    blob = bucket.blob(filename)
    blob.download_to_filename(actual_filename)

def get_signed_url(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("gradder-storage")
    blob = bucket.get_blob(filename)
    return blob.generate_signed_url(expiration=datetime.utcnow() + timedelta(seconds=3600))