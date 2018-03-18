"""
This script defines encoder and decoder models for creating a VAE (variational autoencoder). 
Based on Chapter 8 of "Deep Learning for Python" by Francois Chollet.
By Vineet Sunkavalli
"""

#dependencies
import keras
from keras import layers
from keras import backend as K
from keras.models import Model
import numpy as np

class CustomVariationalLayer(keras.layers.Layer):
    

def encoder(img_dim = (64, 64, 3), latent_dim = 32):

    input = keras.Input(shape=img_dim)

    x = layers.Conv2D(32, 3, padding='same', activation='relu')(input)
    x = layers.Conv2D(64, 3, padding='same', activation='relu')(x)
    x = layers.Conv2D(64, 3, padding='same', activation='relu')(x)
    x = layers.Conv2D(64, 3, padding='same', activation='relu')(x)

    shape = K.int_shape(x)#shape before the network is flattened

    x = layer.Flatten()(x)
    x = layer.Dense(32, activation='relu')(x)

    z_mean = layers.Dense(latent_dim)(x)
    z_var = layers.Dense(latent_dim)(x)#log variance

def sampling(z_mean, z_var):

    epsilon = K.random_normal(shape = (K.shape(z_mean)[0], latent_dim), mean = 0.,stddev=1.)#random sample

    return z_mean + K.exp(z_var) * epsilon


        epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim),
                              mean=0., stddev=1.)
    return z_mean + K.exp(z_log_var) * epsilon

z = layers.Lambda(sampling)([z_mean, z_log_var])

def decoder():

