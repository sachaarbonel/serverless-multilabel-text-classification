from magpie import Magpie
import json
import tensorflow as tf
import logging
import os
import pickle
import numpy as np

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def predict(event,context):
    logger.info('Event : {}'.format(event))
    logger.info('Event text : {}'.format(event['text']))
    text = event['text']
    labels = load_labels()
    magpie = Magpie(
    keras_model='model/keras_model.h5',
    word2vec_model='model/w2v_model',
    scaler='model/scaler',
    labels= labels
    )

    predicted_text = magpie.predict_from_text(text)
    logger.info('Predicted text : {}'.format(predicted_text))

    return {
        "result": np.array(predicted_text).tolist()
    }

def load_labels():
    currentdir = os.path.join(os.getcwd())
    with open(currentdir+'/model/labels.pkl', 'rb') as f:
        labels= pickle.load(f)
    return labels


if __name__ == "__main__":
    predict('', '')