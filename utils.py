'''
Utilities for using in a project scope
'''
import io
import os
import zipfile
import boto3
import botocore
import settings


def get_env_var_or_raise_exception(env_var_name):
    '''
    Get a value of the environment variable or raise an exception if it does not exist
    :param env_var_name: Environment variable name
    '''
    try:
        return os.environ[env_var_name]
    except Exception as _:
        raise Exception('Required environment variable {} not found!'.format(env_var_name))


def create_model_dir():
    '''
    Check target model directory for existence and create it if needed.
    We use /tmp directory, which is according to AWS Limits
    (see http://docs.aws.amazon.com/lambda/latest/dg/limits.html)
    is Ephemeral disk capacity ("/tmp" space) and can be 512 MB big.
    :return: Path of the model directory
    '''
    # Target directory for Magpie model - it must be a subdirectory of /tmp
    # Check target directory for existence and create it if needed.
    model_dir = '/tmp/magpie-model'
    if not os.path.exists(model_dir):
        print('Going to create a model directory {}...'.format(model_dir))
        os.makedirs(model_dir)
        print('...success!')
    print('Model directory is {}'.format(model_dir))

    return model_dir


def download_model_from_bucket(model_dir):
    '''
    Downloads Magpie model from S3 bucket if it was not downloaded yet
    '''
    # check the model file for existence and download if needed
    # protobuf_file_name = get_env_var_or_raise_exception(settings.MODEL_PROTOBUF_FILE_NAME_ENV_VAR)
    # model_path = model_dir + '/' + protobuf_file_name
    #if not os.path.isfile(model_path):
    bucket_name = get_env_var_or_raise_exception(settings.S3_MODEL_BUCKET_NAME_ENV_VAR)
    model_zip_file_name = get_env_var_or_raise_exception(settings.MODEL_ZIP_FILE_NAME_ENV_VAR)
    print('Going to download a model file from S3 bucket {}/{}...'.format(bucket_name, model_zip_file_name))

    # create S3 resource
    s3_res = boto3.resource('s3')
    target_model_zip_path = model_dir + '/' + model_zip_file_name
    try:
        # download ZIP
        s3_bucket = s3_res.Bucket(bucket_name)
        s3_bucket.download_file(model_zip_file_name,target_model_zip_path)

        # extract everything from zip
        with zipfile.ZipFile(target_model_zip_path, 'r') as zip_ref:
            zip_ref.extractall(model_dir)

        # delete zip
        os.remove(target_model_zip_path)

    except botocore.exceptions.ClientError as exception:
        if exception.response['Error']['Code'] == "404":
            print("The object does not exist.")
        if exception.response['Error']['Code'] == "403":
            print("Access denied.")
        raise