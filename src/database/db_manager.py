import pandas as pd
from src.utils.common import read_yaml


class DataBaseManager:
    def __init__(self):
        self.database_config = "src/config/config.yaml"

    def read_prediction_data(self):
        config_ = read_yaml(self.database_config)
        df = pd.read_csv(config_["DATABASE_PATH"])

        return df
