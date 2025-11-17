import joblib
import pandas as pd
import mlflow
from sklearn.metrics import mean_squared_error, r2_score
import math
from mlflow_setup.mlflow_config import init_mlflow

def evaluate(test_path="data/processed/test.csv",
             model_path="data/model/model.pkl"):
    init_mlflow()
    with mlflow.start_run(run_name="model_evaluation"):
        df = pd.read_csv(test_path)
        X_test = df.drop('target', axis=1)
        y_test = df['target']
        model = joblib.load(model_path)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = math.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        mlflow.log_metric("MSE", mse)
        mlflow.log_metric("RMSE", rmse)
        mlflow.log_metric("R2_Score", r2)
        print(f"Model evaluation completed.\nMSE: {mse}\nRMSE: {rmse}\nR2 Score: {r2}")
        return mse, rmse, r2
    
if __name__ == "__main__":
    evaluate()