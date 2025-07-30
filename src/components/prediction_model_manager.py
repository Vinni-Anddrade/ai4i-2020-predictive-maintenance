from src.utils.common import get_best_model_from_artifacts, get_artifact


class PredictionModelManager:
    def __init__(self):
        self.experiment_name = "testing_experiment"
        self.get_best_model()

    def get_best_model(self):
        run_id, model_name, data_type = get_best_model_from_artifacts(
            self.experiment_name
        )
        self.model = get_artifact(run_id, model_name)
        self.data_type = data_type
