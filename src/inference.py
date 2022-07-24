import pandas as pd
import numpy as np
import sys
import os
import mlflow
sys.path.append(os.path.abspath('..'))
from src.preprocess import get_preprocessed_data
from mlflow.tracking import MlflowClient
from dotenv import load_dotenv


def get_best_model():
    if os.getenv('ROOT') is None:
        load_dotenv()

    tracking_uri = os.getenv('ROOT') + '/models/mlruns'
    client = MlflowClient(tracking_uri)

    experiment_name = 'House prices prediction'

    experiment_id = client.get_experiment_by_name(
        experiment_name).experiment_id

    all_runs_info = client.list_run_infos(experiment_id)
    all_runs_id = [run.run_id for run in all_runs_info]
    all_params = [client.get_run(run_id).data.params['random_state'] for run_id
                  in all_runs_id]
    all_metrics = [client.get_run(run_id).data.metrics['rmsle'] for run_id
                   in all_runs_id]

    df = pd.DataFrame(
        {'id': all_runs_id, 'params': all_params, 'metrics': all_metrics})

    best_run_id = df.sort_values('metrics', ascending=True).iloc[0]['id']
    best_model_path = client.download_artifacts(best_run_id,
                                                'random forest regressor')
    print('using model:', best_model_path, 'with id:', best_run_id)
    return mlflow.sklearn.load_model(best_model_path)


def make_predictions(input_data: pd.DataFrame) -> np.ndarray:
    """
    Make predictions on best performing model
    """
    input_data = get_preprocessed_data(input_data, is_train_data=False)

    return get_best_model().predict(input_data)
