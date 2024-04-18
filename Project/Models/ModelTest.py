# this incorporates Keras tuner

import DataParser, keras_tuner, keras
from sklearn.model_selection import train_test_split
from Model import build_model

X = DataParser.posN_Set_X
y =  DataParser.engine_Set_Y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=56)

tuner = keras_tuner.RandomSearch(
    hypermodel=build_model,
    objective="val_accuracy",
    overwrite=True,
    directory="Htuning",
    project_name="Htuning",
)

tuner.search_space_summary()

tuner.search(X_train, y_train, epochs=4, batch_size=262144, validation_data=(X_test, y_test), verbose=2)

best_HP = tuner.get_best_hyperparameters()

# to access these values by code
best_HP.values

print(best_HP)




