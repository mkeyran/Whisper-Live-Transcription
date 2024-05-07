"""
This module contains the user interface for the whisper_live_transcription package.
This interface is a pyside application without ui but with a tray icon that allows the user to start and stop the transcription.
"""

import sys
import os
import logging
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

from whisper_live_transcription.transcribe import Transcriber
from whisper_live_transcription.sound_capture import Capturer
from whisper_live_transcription.output import Output
from whisper_live_transcription.util import setup_logger

logger = setup_logger(__name__)

class WhisperLiveTranscriptionUI:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.transcriber = Transcriber()
        self.capturer = Capturer()
        self.output = Output()
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons", "inactive.png")))
        self.tray_icon.setVisible(True)
        self.tray_icon.setToolTip("Whisper Live Transcription")
        self.menu = QMenu()
        self.start_action = QAction("Start Transcription")
        self.start_action.triggered.connect(self.start_transcription)
        self.menu.addAction(self.start_action)
        self.stop_action = QAction("Stop Transcription")
        self.stop_action.triggered.connect(self.stop_transcription)
        self.stop_action.setEnabled(False)
        self.menu.addAction(self.stop_action)
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.quit)
        self.menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.menu)
        self.app.exec()

    def start_transcription(self):
        self.capturer.start_capture()
        self.start_action.setEnabled(False)
        self.stop_action.setEnabled(True)
        self.tray_icon.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons", "active.png")))

        
    def stop_transcription(self):
        file_names = self.capturer.stop_capture()
        self.tray_icon.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons", "transcribing.png")))
        outputs = self.transcriber.transcribe(file_names)
        self.output.write(outputs)
        self.start_action.setEnabled(True)
        self.stop_action.setEnabled(False)
        self.tray_icon.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons", "inactive.png")))

    def quit(self):
        self.app.quit()

def main():
    WhisperLiveTranscriptionUI()

if __name__ == "__main__":
    main()

