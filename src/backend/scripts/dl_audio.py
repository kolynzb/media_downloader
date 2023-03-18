import youtube_dl 
from .. import history_service


def download_audio1(yt_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '/%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(yt_url, download=True)
        title = info_dict.get('title', None)
        file_name = ydl.prepare_filename(info_dict)
    history_service.save_to_history(title, file_name)


def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(yt_url, download=True)
        title = info_dict.get('title', None)
        file_name = ydl.prepare_filename(info_dict)
    history_service.save_to_history(title, file_name)

# download_audio("https://youtu.be/up7e41593fY")