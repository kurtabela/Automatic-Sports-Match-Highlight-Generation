from youtube_transcript_api import YouTubeTranscriptApi
import urllib.request
import json
import urllib

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

for video in video_URLS:
    # Get the video titles
    params = {"format": "json", "url": video}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        # Get the transcripts
        with open('Transcripts/' + data['title'][17:] + '.json', 'w') as f:
            # The video ID is after the 17th character ("https://youtu.be/"....)
            toInsert = YouTubeTranscriptApi.get_transcript(video[17:])
            toRemove = []
            for text in toInsert:
                if text['text'] == '[Applause]' or text['text'] == '[Music]':
                    toRemove.append(text)
            toInsert = [words for words in toInsert if words not in toRemove]
            print(toInsert, file=f)
