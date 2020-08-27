from keras.models import load_model
model.save("games.h5")
model = load_model('games.h5', custom_objects={'auc': auc})
model.evaluate(x, y, verbose = 0)
