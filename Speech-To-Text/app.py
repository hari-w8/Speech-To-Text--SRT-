import speech_recognition as sr
import time

def recognize_speech_until_understood():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please be quiet. Calibrating microphone for background noise (3 seconds)...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print(f"Minimum energy threshold set to: {recognizer.energy_threshold}")

        while True:
            time.sleep(1)
            print("Start speaking after the beep...")
            time.sleep(1)
            print("Beep! 🎤")
            audio = recognizer.listen(source)

            try:
                print("Processing your speech...")
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                print("Sorry, I couldn’t understand that buddy!!. Speak again...")
            except sr.RequestError as e:
                print(f"API error: {e}")
                break

if __name__ == "__main__":
    recognize_speech_until_understood()
