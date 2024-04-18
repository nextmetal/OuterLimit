import DataParser, keras, sklearn
import numpy as np 

from sklearn.model_selection import train_test_split

X = DataParser.posN_Set_X
y =  DataParser.engine_Set_Y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=56)

model = keras.models.load_model('model0.keras')

print()
print()

y_pred = model.predict(X_test)

print(y_pred)
print(y_test)

for x in range(len(y_pred)):
    if y_pred[x] > 0.5:
        y_pred[x] = 1
    else:
        y_pred[x] = 0


print(y_pred)


print(model.evaluate(X_test, y_test, verbose=2))

print()

print(sklearn.metrics.accuracy_score(y_test, y_pred))