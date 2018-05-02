# Magpie serverless 


Trying to deploy in a serverless fashion this [framework](https://github.com/inspirehep/magpie).
The serverless function works locally but still needs some tweaks to work in the cloud. The model folder contains the pretrained model for the function to work. Pull request highly appreciated.

## Prerequesites

- Have node and npm installed. There is a good guide for installing node and npm on linux [here](https://github.com/creationix/nvm)
- Have python and pip installed. There is a good guide for installing python with conda [here](https://conda.io/docs/user-guide/install/linux.html)
- Have virtualenv installed:
```
 pip install virtualenv
```
- Make sure you have exported your AWS keys in your environmnet variables

## Install / Update serverless framework

```
npm install -g serverless
```

## Getting started

```
git clone https://github.com/Sach97/serverless-multilabel-text-classification.git
cd serverless-multilabel-text-classification
virtualenv venv --python=python3
source venv/bin/activate
pip3 install git+https://github.com/inspirehep/magpie.git@v2.0 && pip3 install tensorflow
serverless invoke local -f predict --data '{"text":"Stephen Hawking studies black holes"}' --log # uncomment the two lines in handler.py
```

## Build the code dependcy package yourself + train model
```
git clone https://github.com/Sach97/serverless-multilabel-text-classification.git
cd serverless-multilabel-text-classification
chmod +x build_vendored.sh
chmod +x clean_venv.sh
chmod +x env_var.sh
virtualenv venv --python=python3
source venv/bin/activate
pip3 install git+https://github.com/inspirehep/magpie.git@v2.0 && pip3 install tensorflow
sh clean_venv.sh
sh build_vendored.sh
python train_model.py
python upload_model.py
serverless invoke local -f predict --data '{"text":"Stephen Hawking studies black holes"}' --log 
```

## Run locally

```
serverless invoke local -f predict --data '{"text":"Stephen Hawking studies black holes"}' --log
```
## TODOs

- [x] Create a real function not just an import magpie
- [x] Make a better shell script for the zip
- [ ] Resolve the [issue](https://github.com/Sach97/serverless-multilabel-text-classification/issues/1)
- [ ] Add [CircleCI](https://serverless.com/blog/ci-cd-workflow-serverless-apps-with-circleci/) continuous integration badge and an explanation guide. 
- [ ] Add an AWS deployment button
- [ ] Load the model globally before a lambda function get called, like in this [repo](https://github.com/Vetal1977/tf_aws_lambda)


