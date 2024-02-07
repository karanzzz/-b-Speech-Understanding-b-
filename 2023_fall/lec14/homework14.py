import datetime
import gtts
import random
import speech_recognition as sr

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M")
    
    # Convert the time to speech
    tts = gtts.gTTS(text=f"It is {current_time}", lang=lang)
    
    # Save the speech to a file
    tts.save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    # List of jokes
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What did one plate say to the other plate? Dinner's on me!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        # Add more jokes as needed
    ]
    
    # Select a random joke
    joke = random.choice(jokes)
    
    # Convert the joke to speech
    tts = gtts.gTTS(text=joke, lang=lang)
    
    # Save the speech to a file
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    
    # Convert the date to speech
    tts = gtts.gTTS(text=f"Today is {current_date}", lang=lang)
    
    # Save the speech to a file
    tts.save(audiofile)
    
    # Return a URL to a calendar website
    return "https://www.calendar.com"

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Start listening
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech
        text = recognizer.recognize_google(audio, language=lang)
        print("You said:", text)
        
        # Check for request
        if "time" in text:
            what_time_is_it(lang, filename)
        elif "day" in text:
            what_day_is_it(lang, filename)
        elif "joke" in text:
            tell_me_a_joke(lang, filename)
        else:
            print("Sorry, I didn't understand that.")
    
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
