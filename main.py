import speech_recognition as sr
import pyttsx3
import os

def init_tts_engine():
    """Initialize the text-to-speech engine with better clarity settings."""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    # Let the user select a voice (Male/Female)
    print("\nChoose a voice:")
    print("1) Male Voice")
    print("2) Female Voice")

    choice = input("Enter your choice (1/2): ").strip()
    if choice == "2":
        engine.setProperty("voice", voices[1].id)  # Female voice
    else:
        engine.setProperty("voice", voices[0].id)  # Male voice (default)

    engine.setProperty("rate", 160)  # Set speech rate for clarity
    engine.setProperty("volume", 1.0)  # Set volume to max
    return engine

def speak(text, engine):
    """Convert text to speech with improved clarity."""
    engine.say(text)
    engine.runAndWait()

def speech_to_text(engine):
    """Recognize speech and convert it to text."""
    recognizer = sr.Recognizer()

    # List available microphones
    microphones = sr.Microphone.list_microphone_names()
    print("\nAvailable Microphones:")
    for index, name in enumerate(microphones):
        print(f"{index}: {name}")

    # Ask the user to select a microphone
    try:
        mic_index = int(input("\nEnter the microphone index (default is 0): ") or "0")
        mic_name = microphones[mic_index]
    except (ValueError, IndexError):
        print("Invalid microphone index. Using default (0).")
        mic_index = 0
        mic_name = microphones[mic_index]

    # Set the file path for saving transcriptions
    file_path = r"C:\Users\Madan\Desktop\Machine_learning2\savedfile.txt"
    folder_path = os.path.dirname(file_path)
    os.makedirs(folder_path, exist_ok=True)  # Ensure the directory exists

    print(f"\nSaving transcriptions to: {file_path}")

    exit_commands = ["exit from listening mode", "exit listening mode", "stop listening", "quit listening"]

    with open(file_path, "a") as file:
        with sr.Microphone(device_index=mic_index) as source:
            print(f"\nUsing microphone: {mic_name}")
            speak("Listening for speech. Say 'exit listening mode' to stop.", engine)
            print("Listening for speech... (Say 'exit listening mode' to stop)")

            recognizer.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    speak(f"You said: {text}", engine)

                    # Save the recognized speech to the file
                    if not any(command in text.lower() for command in exit_commands):
                        file.write(text + "\n")
                    else:
                        print("Exiting listening mode...")
                        speak("Exiting listening mode.", engine)
                        break  # Exit loop

                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand that.")
                    speak("Sorry, I couldn't understand that.", engine)
                except sr.RequestError:
                    print("Could not request results; check your internet connection.")
                    speak("Could not request results. Please check your internet connection.", engine)
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting safely.")
                    speak("User interrupted. Exiting safely.", engine)
                    break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    speak(f"An error occurred: {e}", engine)

    # Open the saved file in Notepad
    os.system(f'notepad.exe "{file_path}"')

def text_to_speech(engine):
    """Convert user-input text to speech."""
    print("\nEnter the text you want to convert to speech:")
    text = input("Text: ")
    speak(text, engine)
    print("\nSpeaking...")

def main():
    """Main function to choose STT or TTS."""
    engine = init_tts_engine()  # Initialize TTS engine

    while True:
        print("\nChoose an option:")
        print("1) Speech-to-Text (STT)")
        print("2) Text-to-Speech (TTS)")
        print("3) Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            speech_to_text(engine)
        elif choice == "2":
            text_to_speech(engine)
        elif choice == "3":
            print("Exiting program...")
            speak("Exiting program.", engine)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            speak("Invalid choice. Please enter 1, 2, or 3.", engine)

if __name__ == "__main__":
    main()
