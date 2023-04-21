from .models import UserProfile, UserSocials
import requests
from pyyoutube import Api
from googleapiclient.discovery import build
from youtubesearchpython import *
import json
import urllib.request as urllib

API_KEY = "AIzaSyAlXVjutqIjSfLLKY8u5rqvSem-ykJMZ-Y"
api = Api(api_key=API_KEY)
youtube = build('youtube', 'v3', 
                developerKey=API_KEY)
def user_details(request):
    links = UserProfile.objects.all()
    return dict(links=links)

def user_socials(request):
    socials = UserSocials.objects.all()
    print(socials)
    return dict(socials=socials)

def user_stats(request):
    ch_request = youtube.channels().list(
    part='statistics',
    id='UCW2kIwAquQA1aj28X3iStYA')
    ch_response = ch_request.execute()
  
    sub = int(ch_response['items'][0]['statistics']['subscriberCount'])
    vid = int(ch_response['items'][0]['statistics']['videoCount'])
    views = int(ch_response['items'][0]['statistics']['viewCount'])
    search_response = youtube.search().list(
        part='id',
        channelId="UCW2kIwAquQA1aj28X3iStYA",
        order='date',
        type='video',
    ).execute()
    video_id = search_response['items'][0]['id']['videoId']
    print(video_id)
    return dict(subs="{:,}".format(sub),vid="{:,}".format(vid),total_views="{:,}".format(views), video_id=video_id)
