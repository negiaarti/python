import sounddevice as sd
import wavio
import os

def record_audio(filename, duration, fs=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    wavio.write(filename, recording, fs, sampwidth=2)
    print(f"Saved recording as {filename}")

def play_audio(filename):
    print("Playing audio...")
    wav = wavio.read(filename)
    sd.play(wav.data, wav.rate)
    sd.wait()  # Wait until audio is done playing
    print("Finished playing audio.")

def main():
    recordings_folder = "recordings"
    if not os.path.exists(recordings_folder):
        os.makedirs(recordings_folder)

    recording_duration = 120  # 2 minutes

    while True:
        action = input("Enter 'r' to record, 'p' to play, 'q' to quit: ").lower()
        if action == 'r':
            filename = input("Enter filename for the recording (without extension): ")
            filepath = os.path.join(recordings_folder, f"{filename}.wav")
            record_audio(filepath, recording_duration)
        elif action == 'p':
            filename = input("Enter filename to play (without extension): ")
            filepath = os.path.join(recordings_folder, f"{filename}.wav")
            if os.path.exists(filepath):
                play_audio(filepath)
            else:
                print("File does not exist.")
        elif action == 'q':
            break
        else:
            print("Invalid input. Please enter 'r', 'p', or 'q'.")

if __name__ == "__main__":
    main()
