import numpy as np
import pyaudio
import time
import os
import sys
import shutil
import tempfile

# --- Automatic DLL Handling for PyInstaller ---
def setup_portaudio_dll():
    if getattr(sys, 'frozen', False):  # Running as EXE
        try:
            # Find portaudio.dll in PyAudio package
            import pyaudio
            pa_dir = os.path.dirname(pyaudio.__file__)
            dll_path = os.path.join(pa_dir, 'portaudio.dll')
            
            if os.path.exists(dll_path):
                # Copy to temp directory and add to PATH
                temp_dir = tempfile.gettempdir()
                temp_dll = os.path.join(temp_dir, 'portaudio.dll')
                shutil.copyfile(dll_path, temp_dll)
                os.environ['PATH'] = temp_dir + os.pathsep + os.environ['PATH']
        except Exception as e:
            print(f"DLL handling warning: {str(e)}")

setup_portaudio_dll()

# --- Audio Generation ---
SAMPLE_RATE = 44100
FREQUENCY = 10  # 10Hz subsonic tone
VOLUME = 0.5    # 50% volume

# Timeline (seconds)
FADE_IN = 4.0
FULL_DURATION = 12.0
FADE_OUT = 4.0
SILENCE_END = 0.5

def generate_tone():
    # Generate each segment separately for precision
    fade_in = np.sin(2 * np.pi * FREQUENCY * 
                   np.linspace(0, FADE_IN, int(SAMPLE_RATE * FADE_IN), False)) * VOLUME
    full = np.sin(2 * np.pi * FREQUENCY * 
                np.linspace(0, FULL_DURATION, int(SAMPLE_RATE * FULL_DURATION), False)) * VOLUME
    fade_out = np.sin(2 * np.pi * FREQUENCY * 
                    np.linspace(0, FADE_OUT, int(SAMPLE_RATE * FADE_OUT), False)) * VOLUME

    # Apply exponential fades
    fade_in *= np.logspace(-5, 0, len(fade_in))
    fade_out *= np.logspace(0, -5, len(fade_out))

    # Combine with silence
    silence = np.zeros(int(SAMPLE_RATE * SILENCE_END))
    return np.concatenate((fade_in, full, fade_out, silence)).astype(np.float32)

# --- Robust Playback System ---
def play_audio():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=SAMPLE_RATE,
        output=True,
        frames_per_buffer=4096  # Larger buffer prevents underruns
    )

    audio_data = generate_tone()
    chunk_size = 4096
    position = 0

    # Chunked playback ensures no premature termination
    while position < len(audio_data):
        chunk = audio_data[position:position + chunk_size]
        stream.write(chunk.tobytes())
        position += len(chunk)

    # Gentle shutdown sequence
    time.sleep(0.1)  # Drain buffer
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    play_audio()