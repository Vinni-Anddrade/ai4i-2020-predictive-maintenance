from src.database.db_manager import DataBaseManager
from src.utils.common import read_yaml
import pandas as pd


class DataReaderManager:
    def __init__(self):
        self.database_config = "src/config/config.yaml"

        self.get_data_for_prediction()
        self.drop_useless_columns()
        self.one_hot_encoding_on_labels()

    def get_data_for_prediction(self):
        db_manager = DataBaseManager()
        self.df = db_manager.read_prediction_data()

    def drop_useless_columns(self):
        config_ = read_yaml(self.database_config)
        cols_to_go = config_["COLUMNS"]

        self.df = self.df.loc[:, cols_to_go]

    def one_hot_encoding_on_labels(self):
        self.df = pd.get_dummies(self.df, dtype=int)
