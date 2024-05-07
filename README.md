# Whisper Live Transcription

This project provides live transcription services.

## Installation

This project uses Poetry for dependency management. To install the project dependencies, run:

```sh
poetry install
```

# Usage

To run the project, execute the following command:

```sh
poetry run whisper-live-transcription
```

The tray icon will appear in the system tray. Right-click on the icon to access the menu.

# Output

The transcription results for now are logged by the Output class in output.py.

# Testing

To run the tests, execute the following command:

```sh
pytest tests/
```

# System Requirements

- Linux OS
- Python 3.9 or higher
- Poetry
- PulseAudio or Pipewire

# License

This project is licensed under the MIT License