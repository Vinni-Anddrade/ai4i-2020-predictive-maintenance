import mlflow


class PredictionManager:
    def __init__(self):
        pass

    def create_model_path(self, uri, model_name):
        model_uri = f"runs:/{uri}/{model_name}"
        return model_uri

    def get_model(self, model_uri):
        self.loaded_model = mlflow.pyfunc.load_model(model_uri)

    def make_prediction(self, df):
        y_pred = self.loaded_model.predict(df)
        return y_pred
