from src.components.prediction_model_manager import PredictionModelManager


class PredictionModelPipeline:
    def __init__(self):
        pass

    def execute_pipeline(self):
        print("\n>>>>>>>>>>>>>>> Starting Artifact Acquisition <<<<<<<<<<<<<<")
        model_manager = PredictionModelManager()

        model = model_manager.model
        data_type = model_manager.data_type

        print("\n>>>>>>>>>>>>>>> Finishing Artifact Acquisition <<<<<<<<<<<<<<")

        return model, data_type
