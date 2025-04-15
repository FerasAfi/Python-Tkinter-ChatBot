from youtube_transcript_api import YouTubeTranscriptApi


def get_transcription(url):
    url = url.split('=')
    video_id = url[1].split('&')
    video_id = video_id[0]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        sub=""
        for line in transcript:
            sub+=line['text']

        return sub
    except Exception as e:
        return e
