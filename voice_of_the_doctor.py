# import os
# from gtts import gTTS
# import subprocess
# import platform
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"
#     audioobj= gTTS(text=input_text, lang=language, slow=False)
#     audioobj.save(output_filepath)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             # Use Windows Media Player COM object instead of SoundPlayer
#             powershell_cmd = (
#                 f'$player = New-Object -ComObject WMPlayer.OCX; '
#                 f'$player.URL="{output_filepath}"; '
#                 f'$player.controls.play(); '
#                 f'Start-Sleep -Seconds 5'  # let it play for a few seconds
#             )
#             subprocess.run(['powershell', '-Command', powershell_cmd])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # or use mpg123 for MP3
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.generate(
#         text=input_text,
#         voice="Aria",
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":
#             powershell_cmd = (
#                 f'$player = New-Object -ComObject WMPlayer.OCX; '
#                 f'$player.URL="{output_filepath}"; '
#                 f'$player.controls.play(); '
#                 f'Start-Sleep -Seconds 5'
#             )
#             subprocess.run(['powershell', '-Command', powershell_cmd])
#         elif os_name == "Linux":
#             subprocess.run(['aplay', output_filepath])
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")
# ========================================================
import os
from gtts import gTTS
import subprocess
import platform
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            powershell_cmd = (
                f'$player = New-Object -ComObject WMPlayer.OCX; '
                f'$player.URL="{output_filepath}"; '
                f'$player.controls.play(); '
                f'Start-Sleep -Seconds 5'
            )
            subprocess.run(['powershell', '-Command', powershell_cmd])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

    return output_filepath   # <— ✅ return the file path


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            powershell_cmd = (
                f'$player = New-Object -ComObject WMPlayer.OCX; '
                f'$player.URL="{output_filepath}"; '
                f'$player.controls.play(); '
                f'Start-Sleep -Seconds 5'
            )
            subprocess.run(['powershell', '-Command', powershell_cmd])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

    return output_filepath   # <— ✅ return the file path