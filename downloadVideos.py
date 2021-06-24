import os
import subprocess

from pytube import YouTube


def downloadVideos():
    # Array of video URLS, from 2010 onwards. Taken from:
    video_URLS = [
        "https://youtu.be/J41d0cHAfSM",
        "https://youtu.be/Xhu5Bz1xDf0",
        "https://youtu.be/KXdVpPYU1As",
        "https://youtu.be/7Fau-IwbuJc",
        "https://youtu.be/ervkVzoFJ5w",
        "https://youtu.be/3fYpcapas0k",
        "https://youtu.be/XojtTwQ3REg",
        "https://youtu.be/5OJfbYQtKtk",
        "https://youtu.be/uuSd4T074iQ",
        "https://youtu.be/a4Lt_hJdvNY",
        "https://youtu.be/eMdTsex8Cyw",
        "https://youtu.be/eMdTsex8Cyw",
        "https://youtu.be/_qFWBYktaRw",
        "https://youtu.be/UAbX7wld9vg",
        "https://youtu.be/U8AcLO8xmkg",
        "https://youtu.be/FXVTSQSSBqI",
    ]

    for video_URL in video_URLS:
        print(video_URL)
        YouTube(video_URL).streams.get_highest_resolution().download("../Datasets/Videos")
        # YouTube(video_URL).streams.filter(only_audio=True).first().download("Audio")


def trimFileNames():
    path = 'C:\Thesis\Datasets\Videos'
    files = os.listdir(path)

    for file in files:
        print(os.path.join(path, file.replace(" ", "")))
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(" ", "")))

    path = 'C:\Thesis\Datasets\Audio'
    files = os.listdir(path)

    for file in files:
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(" ", "")))


def getAudio():
    path = '../Datasets/Videos'
    files = os.listdir(path)
    # files = ['BelgiumvJapan2018FIFAWorldCupFullMatch.mp4']

    for file in files:
        print("Doing: " + file)

        command = "ffmpeg -i " + '../Datasets/Videos/' + file + " -ab 160k -ac 2 -ar 44100 -vn " + "../Datasets/Audio/" + \
                  file.partition(".mp4")[0] + ".mp3"

        subprocess.call(command, shell=True)


if __name__ == '__main__':
    downloadVideos()
    getAudio()
    trimFileNames()
