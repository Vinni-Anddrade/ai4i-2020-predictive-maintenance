from src.components.model_manager import ModelManager


class ModelPipeline:
    def __init__(self):
        pass

    def execute_pipeline(self):
        print("\n>>>>>>>>>>>>>>> Starting Artifact Acquisition <<<<<<<<<<<<<<")
        model_manager = ModelManager()

        model = model_manager.model
        data_type = model_manager.data_type
        run_id = model_manager.run_id
        model_name = model_manager.model_name

        print("\n>>>>>>>>>>>>>>> Finishing Artifact Acquisition <<<<<<<<<<<<<<")

        return model, data_type, run_id, model_name
