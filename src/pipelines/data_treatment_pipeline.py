from src.components.data_treatment_manager import DataTreatmentManager
import pandas as pd


class DataTreatmentPipeline:
    def __init__(self, data_type: str, data: pd.DataFrame):
        self.data_type = data_type
        self.data = data

    def execute_pipeline(self):
        data_treatment_manager = DataTreatmentManager()
        data_treatment_manager.data_treatment(self.data_type, self.data)
        df_prediction = data_treatment_manager.data_to_go

        return df_prediction
