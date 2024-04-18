import keras
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential
from keras.losses import BinaryCrossentropy as BCE



def build_model(hp):
    model = Sequential()

    # input layer
    model.add(keras.layers.InputLayer(input_shape=[71]))

    for i in range(hp.Int("num_layers", 5, 10)):
        model.add(
            Dense(units=hp.Int(f"units {i}", min_value=78, max_value=114, step=18), 
                  activation='relu',
                  )
            )

    # output layer
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile( optimizer=keras.optimizers.Adam(learning_rate=1e-4),
                   loss=BCE(), 
                   metrics=['accuracy', 'precision', 'recall']
                )

    return model