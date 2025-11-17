import os
import mlflow

def init_mlflow():
    os.makedirs("mlruns", exist_ok=True)
    mlflow.set_tracking_uri("http://127.0.0.1:5050")
    mlflow.set_experiment("linear_model_pipeline"
                          )
    return True


# init_mlflow()