#!/bin/bash

touch ./venv/lib/python3.6/site-packages/google/__init__.py

# cleaning unused libs recursively

for dir in "./venv/lib/python3.6/site-packages/"
do
  cd "./venv/lib/python3.6/site-packages/"
  find . -name \*.pyc -delete
  find . -type d -name "__MACOSX" -exec rm -rf {} +
  find . -type d -name "unsupported" -exec rm -rf {} +
  find . -type d -name "thirdparty" -exec rm -rf {} +
  find . -type d -name "external" -exec rm -rf {} +
  find . -type d -name "*_tensorboard*" -exec rm -rf {} +
  find . -type d -name "easy_install" -exec rm -rf {} +
  find . -type d -name "licenses" -exec rm -rf {} +
  find . -type d -name "wheel*" -exec rm -rf {} +
  find . -type d -name "pip*" -exec rm -rf {} +
  find . -type d -name "windows" -exec rm -rf {} +
  find . -type d -name "contrib" -exec rm -rf {} +
  find . -type d -name "__pycache__" -exec rm -rf {} +
  find . -type d -name "setuptools*" -exec rm -rf {} +
  find . -type d -name "tutorial*" -exec rm -rf {} +
  find . -type d -name "*.dist-info" -exec rm -rf {} +
  
done