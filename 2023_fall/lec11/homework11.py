import speech_recognition

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


importlib.reload(homework11)

text = homework11.transcribe_wavefile("264752__copyc4t__phone-messages-english-and-italian.flac")
print(text)
