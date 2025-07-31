from src.pipelines.data_reader_pipeline import PredictionDataReaderPipeline
from src.pipelines.model_artifact_pipeline import ModelPipeline
from src.pipelines.data_treatment_pipeline import DataTreatmentPipeline
from src.pipelines.prediction_pipeline import PredictionPipeline
import pandas as pd


def pipeline_executor():
    reader_manager = PredictionDataReaderPipeline()
    df = reader_manager.execute_pipeline()
    df_initial = df.copy()

    df.drop(["Machine failure"], axis=1, inplace=True)
    model_manager = ModelPipeline()
    model, data_type, run_id, model_name = model_manager.execute_pipeline()

    treatment_manager = DataTreatmentPipeline(data_type, df)
    prediction_data = treatment_manager.execute_pipeline()

    prediction_manager = PredictionPipeline(prediction_data, run_id, model_name)
    output_prediction = prediction_manager.execute_pipeline()

    df["prediction"] = output_prediction
    with pd.ExcelWriter("output_prediction.xlsx") as writer:
        df.to_excel(
            excel_writer=writer,
            sheet_name="Output Prediction",
            index=False,
        )
        df_initial.to_excel(
            excel_writer=writer,
            sheet_name="Initial Data",
            index=False,
        )


if __name__ == "__main__":
    pipeline_executor()
