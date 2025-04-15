import speech_recognition as sr



recognizer = sr.Recognizer()


def listen():
    while True:
        try:
            with sr.Microphone() as m:
                recognizer.adjust_for_ambient_noise(m, duration=3)
                audio = recognizer.listen(m, timeout=8, phrase_time_limit=15)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(text)
                return(text)


        except sr.RequestError as r:
            print(f"Could not request results from Google Speech Recognition service; {r}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")


