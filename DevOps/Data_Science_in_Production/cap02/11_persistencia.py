import mlflow
import mlflow.sklearn

import shutil
model_path = "models/logit_games_v1"
#shutil.rmtree(model_path)
mlflow.sklearn.save_model(model, model_path)
loaded = mlflow.sklearn.load_model(model_path)
loaded.predict_proba(x)



