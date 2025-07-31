from src.components.prediction_manager import PredictionManager


class PredictionPipeline:
    def __init__(self, data, run_id: str, model_name: str):
        self.data = data
        self.run_id = run_id
        self.model_name = model_name

    def execute_pipeline(self):
        prediction_manager = PredictionManager()
        model_uri = prediction_manager.create_model_path(self.run_id, self.model_name)
        prediction_manager.get_model(model_uri)
        prediction = prediction_manager.make_prediction(self.data)

        return prediction
