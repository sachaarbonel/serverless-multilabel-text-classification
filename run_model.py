'''
For test purpose only. Allows loading of a model and an image locally or from S3 bucket,
and making prediction of loaded image
'''
import os
import zipfile
import json

import settings
import utils
import numpy as np
import boto3
from magpie_model import MagpieModel

if __name__ == '__main__':
    model_dir = "/tmp/magpie-model"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    bucket_name = settings.S3_MODEL_BUCKET_NAME_ENV_VAR
    model_zip_file_name = settings.MODEL_ZIP_FILE_NAME_ENV_VAR
    s3_res = boto3.resource('s3')
    target_model_zip_path = model_dir + '/' + model_zip_file_name
    s3_bucket = s3_res.Bucket(bucket_name)
    s3_bucket.download_file(model_zip_file_name,target_model_zip_path)

    # extract everything from zip
    with zipfile.ZipFile(target_model_zip_path, 'r') as zip_ref:
        zip_ref.extractall(model_dir)
        
    # remove zipfile
    os.remove(target_model_zip_path)
    #os.makedirs(model_dir)
    # if not os.path.exists(model_dir):