import mlflow.keras
model_path = "models/keras_games_v1"
mlflow.keras.save_model(model, model_path)
loaded = mlflow.keras.load_model(model_path,
custom_objects={'auc': auc})
loaded.evaluate(x, y, verbose = 0)


