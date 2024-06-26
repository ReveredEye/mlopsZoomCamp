import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

# Script has been modified to autologging with MLflow.
import mlflow


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    rf = RandomForestRegressor(max_depth=10, random_state=0)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_val)

    # rmse = mean_squared_error(y_val, y_pred, squared=False) <-- squared is deprecated.
    rmse = root_mean_squared_error(y_val, y_pred)
    return rmse


if __name__ == '__main__':
    # Initiate autolog and start run with mlflow
    # ---- IMPORTANT: use `mlflow run --no-conda` to use without conda.------
    mlflow.set_tracking_uri('sqlite:///mlflow.db')
    mlflow.set_experiment('nyc-green-taxi-exp')

    # Below sets log_datasets = False to not track training data as data is NumPy array but
    # mlflow expects pandas DataFrames.
    mlflow.autolog(log_datasets = False)
    with mlflow.start_run():
        mlflow.set_tag("developer", "wylie")
        rmse = run_train()
        mlflow.log_metric(rmse)