import boto3
import sys
import os
import settings
import zipfile

DIR_TO_UPLOAD = 'model'

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def upload_s3():

    s3 = boto3.client('s3')
    filename = settings.MODEL_ZIP_FILE_NAME_ENV_VAR+".zip"
    bucket_name = settings.S3_MODEL_BUCKET_NAME_ENV_VAR
    s3.create_bucket(Bucket=bucket_name)
    s3.upload_file(filename, bucket_name, filename)


if __name__ == '__main__':
    zipf = zipfile.ZipFile('{}.zip'.format(settings.MODEL_ZIP_FILE_NAME_ENV_VAR), 'w', zipfile.ZIP_DEFLATED)
    zipdir(DIR_TO_UPLOAD+"/", zipf)
    zipf.close()
    upload_s3()
    os.remove(settings.MODEL_ZIP_FILE_NAME_ENV_VAR+".zip")