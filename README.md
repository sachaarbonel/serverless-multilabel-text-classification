# Tensorflow serverless 



A ready to deploy example repo as explained in this [blog](https://serverless.com/blog/serverless-python-packaging/)

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
chmod +x build_vendored.sh
chmod +x clean_venv.sh
virtualenv venv --python=python3
source venv/bin/activate
pip3 install git+https://github.com/inspirehep/magpie.git@v2.0 && pip3 install tensorflow
sh clean_venv.sh
build_vendored.sh
```

## Run locally
```
serverless invoke local -f predict --data '{"text":"Stephen Hawking studies black holes"}' --log
```
## TODOs

- [x] Create a real function not just an import magpie
- [x] Make a better shell script for the zip
- [ ] Add [CircleCI](https://serverless.com/blog/ci-cd-workflow-serverless-apps-with-circleci/) continuous integration badge and an explanation guide. 
- [ ] Add an AWS deployment button
- [ ] Load the model globally before a lambda function get called, like in this [repo](https://github.com/Vetal1977/tf_aws_lambda)


