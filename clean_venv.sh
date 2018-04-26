#!/bin/bash

touch ./venv/lib/python3.6/site-packages/google/__init__.py

# cleaning unused libs recursively
#dirs="/venv/lib/python3.6/site-packages/"
for dir in "./venv/lib/python3.6/site-packages/"
do
  cd "./venv/lib/python3.6/site-packages/"
  #rm -rf easy_install* pip* pip-* setup_tools* setuptools* wheel* wheel-* examples* tests* external* __MACOSX* unsupported* thirdparty* docker* # Remove unnecessary libraries to save space
  find . -name \*.pyc -delete
  #find -name "*.so" | xargs strip
  #find -name "*.so.*" | xargs strip
  #find -name "*.md*" | xargs strip
  #find . -type d -name "test*" -exec rm -rf {} +
  #find . -type d -name "doc*" -exec rm -rf {} +
  find . -type d -name "__MACOSX" -exec rm -rf {} +
  find . -type d -name "unsupported" -exec rm -rf {} +
  find . -type d -name "thirdparty" -exec rm -rf {} +
  find . -type d -name "external" -exec rm -rf {} +
  find . -type d -name "*_tensorboard*" -exec rm -rf {} +
  #find . -type d -name "docs_api" -exec rm -rf {} +
  find . -type d -name "easy_install" -exec rm -rf {} +
  find . -type d -name "licenses" -exec rm -rf {} +
  #find . -type d -name "ci" -exec rm -rf {} +
  find . -type d -name "wheel*" -exec rm -rf {} +
  find . -type d -name "pip*" -exec rm -rf {} +
  find . -type d -name "windows" -exec rm -rf {} +
  find . -type d -name "contrib" -exec rm -rf {} +
  find . -type d -name "__pycache__" -exec rm -rf {} +
  #find . -type d -name "__check_build" -exec rm -rf {} +
  #find . -type d -name "_build_utils" -exec rm -rf {} +
  #find . -type d -name "benchamrks" -exec rm -rf {} +
  find . -type d -name "setuptools*" -exec rm -rf {} +
  find . -type d -name "tutorial*" -exec rm -rf {} +
  find . -type d -name "*.dist-info" -exec rm -rf {} +
  #find . -type d -name "datasets" -exec rm -rf {} +
  #find . -type d -name "example*" -exec rm -rf {} +
  
done

alias proj = "cd ./venv/lib/python3.6/site-packages/"
proj
output="vendored"
mkdir -p output
zip -r9q ${output}/magpie.zip *