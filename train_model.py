from magpie import Magpie
import pickle
import os


def train():
    
    magpie = Magpie()
    magpie.train_word2vec('data/hep-categories', vec_dim=100)
    magpie.fit_scaler('data/hep-categories')
    magpie.init_word_vectors('data/hep-categories', vec_dim=100)
    labels = ['Gravitation and Cosmology', 'Experiment-HEP', 'Theory-HEP']
    magpie.train('data/hep-categories', labels, test_ratio=0.2, epochs=30)
    magpie.save_model('model/keras_model.h5')
    magpie.save_word2vec_model('model/w2v_model')
    magpie.save_scaler('model/scaler', overwrite=True)
    save_labels(labels,'model/labels')
    
def save_labels(labels,dirname):
    
    currentdir = os.path.join(os.getcwd())
    with open(currentdir+'{}.pkl'.format(dirname), 'wb') as f:
        pickle.dump(labels, f)


if __name__ == "__main__":
    train()