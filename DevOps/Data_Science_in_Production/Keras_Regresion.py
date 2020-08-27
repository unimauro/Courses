import tensorflow as tf
import keras
from keras import models, layers
import matplotlib.pyplot as plt
keras.__version__

x_train, x_test, y_train, y_test = train_test_split(
gamesDF.drop(['label'], axis=1),gamesDF['label'],test_size=0.3)

# define the network structure
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10,)))
model.add(layers.Dropout(0.1))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
# define ROC AUC as a metric
def auc(y_true, y_pred):
auc = tf.metrics.auc(y_true, y_pred)[1]
keras.backend.get_session().run(
tf.local_variables_initializer())
return auc
# compile and fit the model
model.compile(optimizer='rmsprop',
loss='binary_crossentropy', metrics=[auc])
history = model.fit(x_train, y_train, epochs=100, batch_size=100,
validation_split = .2, verbose=0)

loss = history.history['auc']
val_loss = history.history['val_auc']
epochs = range(1, len(loss) + 1)
plt.figure(figsize=(10,6) )
plt.plot(epochs, loss, 'bo', label='Training AUC')
plt.plot(epochs, val_loss, 'b', label='Validation AUC')
plt.legend()
plt.show()


