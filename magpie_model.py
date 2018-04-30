import os
import operator
from magpie import Magpie
import settings
import pickle
import settings

class MagpieModel:
    def __init__(self, model_dir):
        self.magpie = Magpie(
        keras_model=model_dir+'/{}.h5'.format(settings.MODEL_KERAS_FILE_NAME_ENV_VAR),
        word2vec_model=model_dir+'/{}'.format(settings.MODEL_W2V_FILE_NAME_ENV_VAR),
        scaler=model_dir+'/{}'.format(settings.MODEL_SCALER_FILE_NAME_ENV_VAR),
        labels=self.load_labels(model_dir)
        )


    def load_labels(self,model_dir):
        with open(model_dir+'/{}.pkl'.format(settings.MODEL_LABELS_FILE_NAME_ENV_VAR), 'rb') as f:
            labels= pickle.load(f)
        return labels

    def predict_from_text(self,text):
        return self.magpie.predict_from_text(text)
