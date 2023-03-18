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

    # Download the videos from the playlist
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
# download_playlist("https://www.youtube.com/playlist?list=PLw0v7J164Yk8Lj7HplI-rcbB0EFsjZzJx")
