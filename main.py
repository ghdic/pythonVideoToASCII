from image_to_ascii import image_to_ascii, numpy_to_image
from video_to_frame import extract_video_frame
from donwload_youtube import download_youtube_video
import os
from playsound import playsound
import time
import json

with open('settings.json') as f:
    data = json.load(f)
    FRAME = data['FRAME']


youtube_url = input('Input Youtube Video URL(Recommend 1minutes or less) > ')

try:
    title = download_youtube_video(youtube_url)

    print("Extracting Frame...")
    frames = extract_video_frame(f'{title}.mp4')
    ascii_frames = []

    print("Loading...")
    for frame in frames:
        img = numpy_to_image(frame)
        ascii_frames.append(image_to_ascii(img))

    playsound(f'{title}.m4a', False)
    for frame in ascii_frames:
        # pycharm run에서는 파이프로 연결하여 보여주는것으로 cls, clear가 안됌, 터미널에서 해야함
        # os.system('cls')  # window
        os.system('clear')  # linux, mac
        print(frame)
        time.sleep(FRAME/1000)
finally:
    os.remove(f'{title}.mp4')
    os.remove(f'{title}.m4a')