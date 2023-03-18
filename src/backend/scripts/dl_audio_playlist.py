import youtube_dl 
import history_service

def download_audio_playlist(playlist_url):
    """
    Download 🙃audio files from a playlist   
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': False,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'playliststart': 1,
    }

    # Download the audio files from the playlist
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # ydl.download([playlist_url])
        info = ydl.extract_info(playlist_url, download=False)
        for entry in info['entries']:
            title = entry['title']
            filename = ydl.prepare_filename(entry)
            ydl.download([entry['webpage_url']])
            history_service.save_to_history(title, filename)
# Example usage
# download_audio_playlist("https://www.youtube.com/playlist?list=PLw0v7J164Yk_aCDw1E80C8JntN50QrC1r")
