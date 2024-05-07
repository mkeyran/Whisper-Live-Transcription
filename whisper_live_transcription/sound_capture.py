""" This module captures sound from all sound sources and saves it to a temporary file using ffmpeg. """

from whisper_live_transcription.util import setup_logger
import tempfile
import datetime
import ffmpeg
import pulsectl
logger = setup_logger(__name__)


class Capturer():
    def __init__(self) -> None:
        self.capturing = False
        self.filename = None
        self.start_time = None
        self.end_time = None

    def _get_current_pulse_input_device(self):
        with pulsectl.Pulse("whisper_live_transcription") as pulse:
            input = pulse.source_default_get().name
        return input
    
    def _get_current_pulse_output_device(self):
        with pulsectl.Pulse("whisper_live_transcription") as pulse:
            output = pulse.sink_default_get().name + ".monitor"
        return output



    def start_capture(self):
        logger.info("Starting audio capture")
        self.input_device_filename = tempfile.mktemp(suffix=".input.wav")
        self.output_devicefilename = tempfile.mktemp(suffix=".output.wav")
        # get the current pulse input device
        input_device = self._get_current_pulse_input_device()
        # get the current pulse output device
        output_device = self._get_current_pulse_output_device()
        self.start_time = datetime.datetime.now()
        # capture audio using ffmpeg
        in_stream = ffmpeg.input(input_device, f="pulse")
        out_stream = ffmpeg.input(output_device, f="pulse")

        self.process_input = (ffmpeg.
                              filter([in_stream, out_stream], "amix", duration="longest", inputs=2).
                              output(self.input_device_filename).
                              run_async(quiet=True, overwrite_output=True))
        logger.info(f"Process launch cli {' '.join(self.process_input.args)}")
        # self.process_output = ffmpeg.input(output_device.name, f="pulse").output(self.output_devicefilename).run_async(quiet=True, overwrite_output=True)
        self.capturing = True

    def stop_capture(self):
        logger.info("Stopping audio capture")
        # stop capturing audio
        self.capturing = False
        # stop the process
        
        self.process_input.terminate()
        # self.process_output.terminate()
        
        self.process_input.wait()
        # self.process_output.wait()

        self.end_time = datetime.datetime.now()
        return [self.input_device_filename] #, self.output_devicefilename
    
        