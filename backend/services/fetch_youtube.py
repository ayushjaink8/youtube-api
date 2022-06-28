from backend.models import YoutubeData
from backend.settings import YOUTUBE_API_KEYS
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def getnewposts():
    """
    This function would fetch videos from YouTube API.
    """                   
    current_time = datetime.now()                 
    # So that we do not get the videos that are older than 15 minutes.
    fetch_time = current_time - timedelta(minutes=15)
    
    # flag variable ensures the successful fetching of the videos.
    flag=False
    for apikey in YOUTUBE_API_KEYS:
        try:
            print(apikey)
            youtube = build("youtube", "v3", developerKey=apikey)
            # Assuming that the predefined query is 'ball'.
            request = youtube.search().list(
                q="ball",
                part="snippet",
                order="date",
                maxResults=100,
                publishedAfter=fetch_time.isoformat('T', 'seconds')+'Z'
            )
            response = request.execute()
            flag=True
            for obj in response['items']:
                video_id = obj['id']['videoId']
                video_title = obj['snippet']['title']
                description = obj['snippet']['description']
                channel_id = obj['snippet']['channelId']
                channel_title = obj['snippet']['channelTitle']
                published_datetime = obj['snippet']['publishTime']
                thumbnail_url = obj['snippet']['thumbnails']['default']['url']

                # Saving the results in the backend model.
                q = YoutubeData(
                    video_id=video_id,
                    video_title=video_title,
                    description=description,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    published_datetime=published_datetime,
                    thumbnail_url=thumbnail_url
                )
                q.save()

        except HttpError as err:
            err_code = err.resp.status
            if not(err_code == 400 or err_code == 403):
                break          # to use next key if this key is not working.

        if flag:
            break