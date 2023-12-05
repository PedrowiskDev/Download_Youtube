from pytube import YouTube
import os

DEFAULT_SAVE_PATH = "Your path here!"

def download_video(url, save_path):

    try:

        yt = YouTube(url)

        streams = yt.streams

        video = streams.get_highest_resolution()

        video.download(output_path=save_path)

        print("Download complete!")

    except Exception as e:
        print("An error occurred:", str(e))

video_url = input("Enter the YouTube video URL: ")

save_path = input("Enter the path where you want to save the video (leave blank to use default): ")

if not save_path:
    save_path = DEFAULT_SAVE_PATH

os.makedirs(save_path, exist_ok=True)

download_video(video_url, save_path)
