from src.components.data_reader_manager import DataReaderManager


class PredictionDataReaderPipeline:
    def __init__(self):
        pass

    def execute_pipeline(self):
        print("\n>>>>>>>>>>>>>>> Starting Reading Data <<<<<<<<<<<<<<")
        reader = DataReaderManager()
        df = reader.df
        print("\n>>>>>>>>>>>>>>> Finishing Reading Data <<<<<<<<<<<<<<")

        return df
