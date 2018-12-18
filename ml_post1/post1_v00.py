import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
from keras import optimizers

# read and process data:
data1 = pd.read_csv('sensis_output_ready.csv')
data2 = data1.drop(data1.columns[data1.columns.str.contains('unnamed',case = False)],axis = 1)

X = data2.drop(['PVFP'], axis=1).as_matrix()
prep_X = preprocessing.normalize(X)

y = data2.PVFP

X_train, X_test, y_train, y_test = train_test_split(prep_X, y, test_size=0.1,random_state=42)
n_cols = X_train.shape[1]

# set-up network
model = Sequential()
model.add(Dense(100,  input_shape = (n_cols,)))
model.add(Dense((100)))
model.add(Dense((100)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_absolute_percentage_error', metrics = ['mean_absolute_percentage_error'])

# train & evaluate network
model_training = model.fit(X_train, y_train,epochs = 120, verbose = 2)
model.evaluate(X_test, y_test)

# show the training's history on a diagram
plt.plot(model_training.history['mean_absolute_percentage_error'], 'r')
plt.xlabel('Epochs')
plt.ylabel('mean_absolute_percentage_error')
plt.show()
