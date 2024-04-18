import DataParser, keras
from sklearn.model_selection import train_test_split

from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential

from keras.losses import BinaryCrossentropy as BCE
from keras import regularizers

keras.utils.set_random_seed(56)



# pip installs used (-u upgrades to latest version)
# pip install -U keras
# pip install -U scikit-learn
# pip install -U tensorflow
# pip install -U keras-tuner



model = Sequential()

X = DataParser.posN_Set_X
y =  DataParser.engine_Set_Y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=56)

# Model 0 training accuracy- 86, test accuracy- 70, 
# Model 0 design-no dropout layers, 78,96,114,114,96,114,114,96, 8 hidden layers 

# Model 1 -Failed attempt at regularization

# Model 2 training accuracy- 87, test accuracy- 64, (overfitting)
# Model 2 design-no dropout layers, 78,96,114,114,96,114,114,96,114,114,96, 11 hidden layers 

# Model 3 training accuracy- 86, test accuracy- 67,
# Model 3 design-no dropout layers, 78,96,114,114,96,114,114,96,114,114,96,114,114,96,114,114,96, 17 hidden layers 

# Model 4 training accuracy- 86, test accuracy- 67, 3 regularizing layers (first 3 '96' layers)
# Model 4 design-no dropout layers, 78,96,114,114,114,96,114,114,114,96,114,114,96, 13 hidden layers 

model.add(keras.layers.InputLayer(input_shape=[71]))

model.add(Dense(units=78, activation='relu'))

model.add(Dense(units=96, activation='relu',
        kernel_regularizer=regularizers.L2(0.01)))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))

model.add(Dense(units=96, activation='relu',
        kernel_regularizer=regularizers.L2(0.01)))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))

model.add(Dense(units=96, activation='relu',
        kernel_regularizer=regularizers.L2(0.01)))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))

model.add(Dense(units=96, activation='relu',
        kernel_regularizer=regularizers.L2(0.01)))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))
model.add(Dense(units=114, activation='relu'))

model.add(Dense(units=78, activation='relu'))

model.add(Dense(units=1, activation='sigmoid'))

print()
print()

# Adam optimizer is used as it converges faster

model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-4),
              loss=BCE(),
              metrics=['accuracy', 'precision', 'recall']
              )

model.fit(X_train, y_train, epochs=20000, batch_size=8192, verbose = 2)

print()
print()

print(model.evaluate(X_test, y_test, verbose=2))

model.save('model5.keras')


