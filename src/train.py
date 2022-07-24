import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import Dict
import mlflow
from src.preprocess import get_preprocessed_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_log_error
import os
from dotenv import load_dotenv
import sklearn.metrics as metrics


def compute_rmsle(y_test: np.ndarray, y_pred: np.ndarray,
                precision: int = 2) -> float:
    rmsle = np.sqrt(mean_squared_log_error(y_test, y_pred))
    return round(rmsle, precision)


def evaluate_rmsle(model: RandomForestRegressor, x_test: pd.DataFrame,
                y_test: np.ndarray) -> float:
    y_pred = model.predict(x_test)
    return compute_rmsle(np.array(y_test), np.array(y_pred), 3)


def build_model(data: pd.DataFrame, run_name: str) -> Dict[str, str]:
    if os.getenv('ROOT') is None:
        load_dotenv()

    experiment_name = 'House prices prediction'

    mlflow.set_tracking_uri(os.getenv('ROOT') + '/models/mlruns')

    if not mlflow.get_experiment_by_name(experiment_name):
        mlflow.create_experiment(name=experiment_name)
    experiment = mlflow.get_experiment_by_name(experiment_name)

    with mlflow.start_run(experiment_id=experiment.experiment_id,
                        run_name=f"run_{run_name}"):
        rand_state = np.random.randint(1, 100)

        y = data['SalePrice']
        x = data.drop(columns=['SalePrice'])

        train, test, y_train, y_test = train_test_split(x, y, random_state=rand_state)

        train = get_preprocessed_data(train, is_train_data=True)
        test = get_preprocessed_data(test, is_train_data=False)

        model = RandomForestRegressor(n_estimators=40, random_state=0)
        model.fit(train, y_train)

        y_pred = model.predict(test)

        test_metrics = {
            'mse': metrics.mean_squared_error(y_test, y_pred),
            'msle': metrics.mean_squared_log_error(y_test, y_pred),
            'rmsle': evaluate_rmsle(model, test, y_test)
        }

        params = model.get_params()

        mlflow.sklearn.log_model(model, 'random forest regressor')
        mlflow.log_params(params)
        mlflow.log_metrics(test_metrics)

    return test_metrics
