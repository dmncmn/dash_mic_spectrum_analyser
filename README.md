# dash_mic_spectrum_analyser
Dash Microphone Spectrum Analyser

Application for real-time plotting sound spectrum from a built-in PC microphone based on Dash + Numpy + pyaudio.
The logic of work is the same as that of the desktop version (see mic_spectrum_analyser).

Control:
* Sensitivity (left slider)
* Spectrum resolution (right slider)

Make venv (python==3.9):
```
python -m venv venv
```
Activate:
```
. venv/bin/activate # Linux
venv\Scripts\activate # Win
```

Install requirements:
```
pip install -r requirements.txt
```

Run app (enable microphone):
```
python -m main
```

Open in browser:
```
http://127.0.0.1:8050/
```

Run tests:
```
python -m pytest tests/ -v
```

Screenshots:

![Image alt](https://github.com/dmncmn/dash_mic_spectrum_analyser/blob/main/images/1.PNG)
