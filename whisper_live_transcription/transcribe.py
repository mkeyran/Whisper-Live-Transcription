"""This is a module that contains a class that uses Transformers and the whisper model to transcribe audio file."""

from faster_whisper import WhisperModel
from whisper_live_transcription.util import setup_logger
from datetime import datetime
logger = setup_logger(__name__)

class Transcriber():
    def __init__(self):
        model_size = "large-v3"
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")
        logger.info(f"Model {model_size} loaded successfully.")

    def transcribe(self, files_path: list[str]):   
        start_time = datetime.now()
        logger.info("Transcribing audio file file_path")
        outputs = {}
        for file_path in files_path:
            outputs[file_path] = self.model.transcribe(file_path, beam_size=5, vad_filter=True)
        end_time = datetime.now()
        logger.info(f"Transcription complete. Time taken: {end_time - start_time}")
        return outputs
