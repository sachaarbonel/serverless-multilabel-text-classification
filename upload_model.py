import boto3
import sys
import os
import settings
import zipfile
import glob

DIR_TO_UPLOAD = 'model'

def zipdir(ziph):
    # ziph is zipfile handle
    for name in glob.glob("model/*"):
        ziph.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        

def upload_s3():

    s3 = boto3.client('s3')
    filename = settings.MODEL_ZIP_FILE_NAME_ENV_VAR
    bucket_name = settings.S3_MODEL_BUCKET_NAME_ENV_VAR
    s3.create_bucket(Bucket=bucket_name)
    s3.upload_file(filename, bucket_name, filename)


if __name__ == '__main__':
    zipf = zipfile.ZipFile(settings.MODEL_ZIP_FILE_NAME_ENV_VAR, 'w', zipfile.ZIP_DEFLATED)
    zipdir(zipf)
    zipf.close()
    upload_s3()
    os.remove(settings.MODEL_ZIP_FILE_NAME_ENV_VAR)