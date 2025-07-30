import mlflow
import mlflow.artifacts
import yaml
from box import ConfigBox
from ensure import ensure_annotations
import pickle


TRACKING_URI = (
    "file:///C:/development/equipament-maintenance-prediction/notebooks/mlruns"
)


@ensure_annotations
def register_experiment(
    model: pickle,
    accuracy_score: float,
    recall_score: float,
    f1_score: float,
    run_name: str,
    experiment: str,
    type: str,
) -> None:
    print("\n>>>>>>>>>>> Registering Experiment <<<<<<<<<<<<")
    mlflow.set_experiment(experiment_name=experiment)
    with mlflow.start_run(run_name=run_name):
        mlflow.sklearn.log_model(sk_model=model)

        mlflow.log_metric("accuracy_score", accuracy_score)
        mlflow.log_metric("f1_score", f1_score)
        mlflow.log_metric("recall_score", recall_score)

        mlflow.set_tag("Experiment Type", "Testing")
        mlflow.set_tag("Data Type", type)
    print("\n>>>>>>>>>>> Experiment Registered <<<<<<<<<<<<")


@ensure_annotations
def read_yaml(config_path: str) -> ConfigBox:
    with open(config_path, "r") as file:
        yaml_file = yaml.safe_load(file)
        yaml_output = ConfigBox(yaml_file)

        return yaml_output


@ensure_annotations
def get_best_model_from_artifacts(experiment_name: str):
    mlflow.set_tracking_uri(uri=TRACKING_URI)
    experiment = mlflow.get_experiment_by_name(experiment_name)
    runs = mlflow.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=["metrics.recall_score DESC"],
        max_results=1,
    )

    best_run = runs.iloc[0]
    run_id = best_run["run_id"]
    data_type = best_run["tags.Data Type"]
    model_name = best_run["tags.mlflow.runName"]

    return run_id, model_name, data_type


@ensure_annotations
def get_artifact(run_id: str, model_name: str):
    mlflow.set_tracking_uri(uri=TRACKING_URI)

    logged_model = f"runs:/{run_id}/{model_name}"
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    return loaded_model
