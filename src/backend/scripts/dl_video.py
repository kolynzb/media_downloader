import youtube_dl

def download_playlist(playlist_url):
    """
    Download videos from a playlist
    """
    # Set up the options for youtube_dl
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': False,
        'quiet': True,
        'playliststart': 1,
    }

    youtube_dl.YoutubeDL(ydl_opts)