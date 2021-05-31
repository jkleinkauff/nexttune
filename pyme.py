import os
from keras.models import Model, load_model

# load model
mod = "/home/jhonatas/development/iaa-music-discovery/scratches/multi_perceptron/saved_model/perceptron.h5"
if not os.path.isfile(mod):
    print("me")

model = load_model(mod)