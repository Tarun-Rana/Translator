from vosk import Model, KaldiRecognizer
import pyaudio
    
model = Model(r"E:\Translator\speech-recognition\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)
    
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
while True:
        data = stream.read(4096)
        
    
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(f"' {text[14:-3]} '")