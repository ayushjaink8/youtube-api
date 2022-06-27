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
    # Set the posts which were posted 1000 minutes from current_time
    fetch_time = current_time - timedelta(minutes=1000)
    
    # flag variable ensures the successful fetching of the videos.
    flag=False
    for apikey in YOUTUBE_API_KEYS:
        try:
            youtube = build("youtube", "v3", developerKey=apikey)
            # Assuming that the predefined query is 'football'.
            req = youtube.search().list(
                q="football",
                part="snippet",
                order="date",
                maxResults=50,
                publishedAfter=fetch_time.isoformat('T', 'seconds')+'Z'
            )
            response = req.execute()
          
            flag=True
            for obj in response['items']:
                video_id = obj['id']['videoId']
                video_title = obj['snippet']['title']
                description = obj['snippet']['description']
                channel_id = obj['snippet']['channelId']
                channel_title = obj['snippet']['channelTitle']
                published_datetime = obj['snippet']['publishTime']
                thumbnail_url = obj['snippet']['thumbnails']['default']['url']

                # Saving the results in the backend model
                YoutubeData.objects.create(
                    video_id=video_id,
                    video_title=video_title,
                    description=description,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    published_datetime=published_datetime,
                    thumbnail_url=thumbnail_url
                )

        except HttpError as err:
            err_code = err.resp.status
            if not(err_code == 400 or err_code == 403):
                continue  # to use next key if this key is not working.

        if flag:
            break