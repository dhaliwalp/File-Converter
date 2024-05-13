from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        stream.download(output_path=output_path, filename=output_path)
        return True
    except Exception as e:
        print(f"Error downloading YouTube video: {e}")
        return False

def convert_to_mp3(video_path, output_path):
    try:
        video = VideoFileClip(video_path)
        mp3_output_path = output_path + '.mp3'
        audio = video.audio
        audio.write_audiofile(mp3_output_path)
        audio.close()
        video.close()
        return mp3_output_path
    except Exception as e:
        print(f"Error converting video to MP3: {e}")
        return None
