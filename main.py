from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
import pytube
import os
import requests
from bs4 import BeautifulSoup




isVidorPlay = input('do you to download a video or playlist (video / playlist): ')


if isVidorPlay.lower() == 'video':
    video = input('Enter the video URL: ')
    yt = YouTube(video, on_progress_callback= on_progress)
    os.mkdir(yt.title)
    yt.streams[0].download(yt.title, filename=yt.title)
    x = input('press ENTER to exit...')

elif isVidorPlay.lower() == 'playlist':
    count = 1
    playlist_input = input('Enter the playlist URL: ')
    playlist = Playlist(playlist_input)
    r = requests.get(playlist_input)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')
    foldername = soup.title.string
    os.mkdir(foldername)
    for vid in playlist:
        yt = YouTube(vid, on_progress_callback= on_progress)
        name = str(count)+'__'
        yt.streams[0].download(foldername, filename=name + yt.title)
        print('\n')
        print('Video number ' + str(count) + ' is completed')
        print('\n')
        count += 1
    local = os.getcwdb()
    print('Downloading done. You will find the playlist in "'+ str(local) +'"')
    x = input('press ENTER to exit...')



'''
playlist = Playlist('https://www.youtube.com/playlist?list=PLFKON3XmVv1C8DDfYITN7wW3Jn3C3lNtK')
count = 0
#location = input('enter location: ')
for vid in playlist:
    yt = YouTube(vid)
    name = str(count)+'__'
    yt.streams[0].download('/home/topo/Desktop/',filename=name+yt.title)
    print("it's done")
    count += 1
'''
