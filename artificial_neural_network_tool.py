import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


class artificial_neural_network_algorithm:
    def model_ann(X_train, y_train, X_test, y_test, params):
        try:
            if params == None:
                epochs_custom = 20
            else:
                epochs_custom = int(params['epochs'])
            X_train = np.matrix(X_train)
            y_train = np.array(y_train)
            X_test = np.matrix(X_test)
            y_test = np.array(y_test)
            model = keras.Sequential([
                keras.layers.Dense(128, activation='relu'),
                keras.layers.Dense(7)
            ])
            model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(
                from_logits=True), metrics=['accuracy'])
            model.fit(X_train, y_train, epochs=epochs_custom)
            test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
            evalution = test_acc * 100
            error = ""
            return model, evalution, error
        except Exception as e:
            print(e)
            model = ""
            error = "can't create model with artifical neural network"
            evalution = "evalution = 0.0 [error] create model"
            return(model, evalution, error)
    pass
