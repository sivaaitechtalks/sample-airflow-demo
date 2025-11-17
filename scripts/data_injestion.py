import os
import pandas as pd
from sklearn.datasets import make_regression
import mlflow
from mlflow_setup.mlflow_config import init_mlflow

def ingest(output_path="data/raw/data.csv", n_samples=500, n_features=5, noise=10.0):
    """
    Generate a synthetic regression dataset and save it to a CSV file.

    Parameters:
    - output_path (str): The file path where the CSV will be saved.
    - n_samples (int): Number of samples to generate.
    - n_features (int): Number of features.
    - noise (float): Standard deviation of the Gaussian noise added to the output.
    - random_state (int): Random seed for reproducibility.
    """
    # Generate synthetic regression data
    init_mlflow()
    with mlflow.start_run(run_name="data_ingestion"):
        X, y = make_regression(n_samples=n_samples, n_features=n_features, noise=noise, random_state=42)
        
        # Create a DataFrame
        feature_columns = [f"feature_{i+1}" for i in range(n_features)]
        df = pd.DataFrame(X, columns=feature_columns)
        df['target'] = y
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        
        # Log parameters and artifact to MLflow
        mlflow.log_param("n_samples", n_samples)
        mlflow.log_param("n_features", n_features)
        mlflow.log_param("noise", noise)
        mlflow.log_artifact(output_path)
        
        print(f"Data ingested and saved to {output_path}"
              )
        return output_path
    
    if __name__ == "__main__":
        ingest()