from src.pipelines.data_reader_pipeline import PredictionDataReaderPipeline
from src.pipelines.model_artifact_pipeline import PredictionModelPipeline


def pipeline_executor():
    reader_manager = PredictionDataReaderPipeline()
    df = reader_manager.execute_pipeline()

    model_manager = PredictionModelPipeline()
    model, data_type = model_manager.execute_pipeline()
    print(model, data_type)

    ## Criar o pipeline de limpeza/escalar os dados (Mas tem que seguir o Data type)

    ## Criar o pipeline de predição


if __name__ == "__main__":
    pipeline_executor()
