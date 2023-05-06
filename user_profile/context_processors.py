from .models import UserProfile, UserSocials, UserYT
import requests
from pyyoutube import Api
from googleapiclient.discovery import build
from youtubesearchpython import *
import json
import urllib.request as urllib
import datetime 
import time 
import random

API_KEY = "AIzaSyD4r1LJPBHxWGnbHdiA8ytUo05DxRruUas"

def user_details(request):
    links = UserProfile.objects.all()
    for i in links:
        print(i)
    return dict(links=links)

def user_socials(request):
    socials = UserSocials.objects.all()
    print(socials)
    return dict(socials=socials)

def user_stats(request):
    # video_count = models.TextField(blank=True)
    # video_views = models.TextField(blank=True)
    # subscribers = models.TextField(blank=True)
    # recent_video = models.TextField(blank=True)
    now = datetime.datetime.now()

    try:
        if now.hour % 2 == 0 and now.minute == 0 and now.second <= 60 or request.user.is_authenticated:
            stats = UserYT.objects.all()
            if stats == None:
               UserYT.objects.all().update(video_count = 0, recent_video=0, subscribers=0 , video_views=0, update=False)
            UserYT.objects.all().update(update=True)
            x = UserYT.objects.all()
            for i in x: 
                if i.update:
                    youtube = build('youtube', 'v3', 
                                developerKey=API_KEY)
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
                    UserYT.objects.all().update(video_count = vid, recent_video=video_id, subscribers=sub , video_views=views, update=False)
                    stats = UserYT.objects.all()
                    print("h2222")
                    return dict(stats=stats)
        else:
            print("hi")
            stats = UserYT.objects.all()
            return dict(stats=stats)
    except Exception:
        print("hi")
        stats = UserYT.objects.all()
        return dict(stats=stats)
        