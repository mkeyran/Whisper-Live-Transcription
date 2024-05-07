from whisper_live_transcription.util import setup_logger

logger = setup_logger(__name__)

class Output:
    def __init__(self):
        pass

    def write(self, outputs):
        logger.info("Writing output")
        for k, v in outputs.items():
            logger.info(f"Output for {k}")
            segments = v[0]
            segments_text = "\n".join([f"{segment.start} - {segment.end}: {segment.text}" for segment in segments])
            logger.info(f"Output for {k}: {segments_text}")