from google.cloud import storage
from app.logs.form_logger import form_logger

def upload_blob(bucket_name, filename, file_obj):
    print(file_obj)
    storage_client = storage.Client()
    bucket = storage_client.bucket('gradder-storage')
    blob = bucket.blob(filename)
    blob.upload_from_file(file_obj)
    form_logger.info('File {} uploaded'.format(filename))
    return blob