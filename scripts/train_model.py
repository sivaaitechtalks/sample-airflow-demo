import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
from mlflow_setup.mlflow_config import init_mlflow

def train(train_path="data/processed/train.csv",
          model_output_path="data/model/model.pkl"):
    init_mlflow()
    with mlflow.start_run(run_name="model_training"):
        os.makedirs(os.path.dirname(train_path), exist_ok=True)
        df = pd.read_csv(train_path)
        X = df.drop('target', axis=1)
        y = df['target']
        model = LinearRegression()
        model.fit(X, y)
        os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
        joblib.dump(model, model_output_path)
        mlflow.log_artifact(model_output_path)
        mlflow.log_param("model_type", "LinearRegression")
        print("Model training completed. Model saved at:", model_output_path)
        return model_output_path
    
if __name__ == "__main__":
    train()