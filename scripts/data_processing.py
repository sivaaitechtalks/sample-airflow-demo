import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import mlflow
from mlflow_setup.mlflow_config import init_mlflow


def process(input_path="data/raw/data.csv",
            output_train = "data/processed/train.csv",
            output_test = "data/processed/test.csv"):
    init_mlflow()
    with mlflow.start_run(run_name="data_processing"):
        os.makedirs(os.path.dirname(output_train), exist_ok=True)
        df = pd.read_csv(input_path)
        df = df.dropna()
        X = df.drop('target', axis=1)
        y = df['target']    
        scalar = StandardScaler()
        X_scaled = scalar.fit_transform(X)
        df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
        df_scaled['target'] = y.values
        train_df, test_df = train_test_split(df_scaled, test_size=0.2, random_state=42)
        train_df.to_csv(output_train, index=False)
        test_df.to_csv(output_test, index=False)
        mlflow.log_artifact(output_train)
        mlflow.log_artifact(output_test)
        mlflow.log_param("test_size", 0.2)
        print("Data processing completed. Train and test datasets saved."
              )
        return output_train, output_test
if __name__ == "__main__":
    process()
        
