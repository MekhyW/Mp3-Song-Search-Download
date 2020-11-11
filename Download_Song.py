from pytube import YouTube
import requests
import subprocess
import os

while True:
    try:
        topic = input("Type a song name to Search and Download: ")
        print('>>>Finding song with query "{}"...'.format(topic))
        count = 0
        lst = str(requests.get('https://www.youtube.com/results?q=' + topic).content).split('"')
        for i in lst:
            count+=1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count-5] == "/results":
            print("Sorry, I couldn´t find a song matching that query...")
            raise Exception("No video found.")
        print('>>>Song found!')
        print('>>>Downloading...')
        video = YouTube("https://www.youtube.com"+lst[count-5]).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download()
        print('>>>Conversion process...')
        default_filename = video.default_filename
        new_filename = default_filename.split(".")[0] + ".mp3"
        subprocess.call(["ffmpeg", "-i", default_filename, new_filename])
        os.remove(default_filename)
        print('\nDone! (Check program folder))\n\n')
    except:
        pass