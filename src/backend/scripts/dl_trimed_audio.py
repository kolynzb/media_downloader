import os
import youtube_dl
from pydub import AudioSegment
from datetime import datetime, timedelta

# Define the function to download and trim the audio
def download_and_trim(yt_url, start_time, end_time):
    # Convert the start and end times to milliseconds
    start_time = datetime.strptime(start_time, '%H:%M:%S')
    end_time = datetime.strptime(end_time, '%H:%M:%S')
    start_ms = (start_time - datetime(1900, 1, 1)).total_seconds() * 1000
    end_ms = (end_time - datetime(1900, 1, 1)).total_seconds() * 1000

    # Set up the options for youtube_dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(id)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
    }

    # Download the audio from the YouTube URL
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(yt_url, download=True)
        video_id = info_dict.get("id", None)
        filename = f"{video_id}.mp3"

    # Load the downloaded audio into pydub
    sound = AudioSegment.from_file(filename)

    # Trim the audio based on the start and end times
    trimmed_sound = sound[start_ms:end_ms]

    # Save the trimmed audio to a file
    trimmed_filename = f"{video_id}_{start_time.strftime('%H%M%S')}-{end_time.strftime('%H%M%S')}.mp3"
    trimmed_sound.export(trimmed_filename, format="mp3")

    # Clean up the downloaded file
    os.remove(filename)

# Example usage
# download_and_trim("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "00:00:10", "00:00:20")
