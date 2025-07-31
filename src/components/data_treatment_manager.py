from sklearn.preprocessing import MinMaxScaler
import pandas as pd


class DataTreatmentManager:
    def __init__(self):
        pass

    @staticmethod
    def scale_data(data: pd.DataFrame):
        scaler = MinMaxScaler(feature_range=(0, 1))

        scaled_data = scaler.fit_transform(data.copy())
        return scaled_data

    def data_treatment(self, data_type: str, data: pd.DataFrame):
        if data_type == "Scaled data":
            self.data_to_go = self.scale_data(data)
        else:
            self.data_to_go = data
