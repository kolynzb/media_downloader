import youtube_dl

def download_subtitles(url, lang_code='en'):
    # Create a YouTubeDL instance
    ydl = youtube_dl.YoutubeDL()

    # Extract the video information
    info = ydl.extract_info(url, download=False)

    # Get the available subtitles
    subtitles = info.get('subtitles')

    if subtitles:
        if lang_code in subtitles:
            # Download the subtitle file
            subtitle_url = subtitles[lang_code]['url']
            ydl.download([subtitle_url])
            print("Subtitles downloaded successfully.")
        else:
            print(f"No subtitles found in language '{lang_code}' for this video.")
    else:
        print("No subtitles found for this video.")
