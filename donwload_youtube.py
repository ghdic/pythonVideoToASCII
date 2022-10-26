from pytube import YouTube
import re

def on_complete(stream, file_path):
    print(stream)
    print(file_path)


def on_progress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))


def download_youtube_video(url):
    yt = YouTube(url, on_complete_callback=on_complete, on_progress_callback=on_progress)

    title = re.sub('[\/:*?"<>|]', '', yt.title)

    # progressive=True는 영상과 소리가 같이 있는 영상
    video_filter = yt.streams.filter(mime_type="video/mp4", res="720p", progressive=False)
    print('======= Video Download Start ========')
    video_filter.first().download(filename=f'{title}.mp4')

    print('======= Sound Download Start ========')
    sound_filter = yt.streams.filter(mime_type="audio/mp4", abr="128kbps")
    sound_filter.first().download(filename=f'./{title}.m4a')

    return title


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=Rcq-ywfCWHs'
    # 아래와 같은 에러가 나는 경우(MacOS)
    # urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
    # terminal command "open /Applications/Python\ <python version>/Install\ Certificates.command"
    yt = YouTube(url)

    for stream in yt.streams:
        print(stream)

    # yt.streams.get_highest_resolution().download(DOWNLOAD_DIR)
    # yt.streams.get_lowest_resolution().download(DOWNLOAD_DIR)
    # yt.streams.get_audio_only().download(DOWNLOAD_DIR)

    video_filter = yt.streams.filter(mime_type="video/mp4", res="720p", progressive=True)

    for stream in video_filter:
        print(stream)