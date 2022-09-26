#!/usr/bin/env python

# Youtube music downloader

import argparse
import sys
import youtube_dl

NUM_MUSIC = 5 # Default number of music per channel
CH_URL = "https://www.youtube.com/c/%(channel)s/videos"
CH_URL_OLD = "https://www.youtube.com/channel/%(channel)s/videos" 
CHANNELS_LIST = []
AUTO = False
IMPORT_CONF = True
LOCATION = "Music"
OUTPUT_LOCATION = "%(title)s-%(id)s.%(ext)s"

# Parse arguments
def set_args():
    global IMPORT_CONF, CHANNELS_LIST, NUM_MUSIC, AUTO
    parser = argparse.ArgumentParser(description="Youtube music downloader")
    parser.add_argument("-n", "--number",help="Number of music per channel", type=int)
    parser.add_argument("-a", "--auto", help="Automatically download new music that are not already downloaded", action="store_true")
    parser.add_argument("-u", "--user", help="Download music from a specified user", type=str)
    args = parser.parse_args()

    if args.auto:
        AUTO = args.auto
        NUM_MUSIC = 30
    else:
        NUM_MUSIC = 1
        
    if args.user:
        IMPORT_CONF = False
        CHANNELS_LIST.append(args.user)
    if args.number:
            NUM_MUSIC = args.number
class Downloader:
    def __init__(self,channelsList):
        self.num_music = NUM_MUSIC
        self.channelsList = channelsList
    
    # Download music from a list of channels
    def run(self):
        print("\n##### Youtube Music Downloader #####")
        for channel in self.channelsList:
            print("\n-> Downloading from: %s" % channel)
            channel_url = self.get_channel_url(channel)
            # Check the operating system for windows or linux
            self.download(channel_url,self.num_music)
        print("\n-> Download complete!")
        print("\n####################################")
    
    # Get channel URL
    def get_channel_url(self,channel):
        if len(channel) == 24:
            return  CH_URL_OLD % vars()
        else:
            return  CH_URL % vars()
    
    # Download music from a channel
    def download(self,channel_url,num_music):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': LOCATION+"\%(uploader)s\%(title)s-%(id)s.%(ext)s",
            'playlistend': num_music,
            'playlistreverse': True,
            'download_archive': 'downloaded.txt',
            'consoletitle': True,
            'continuedl': True,
            'quiet': True,
            'forcetitle': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        youtube_dl.YoutubeDL(ydl_opts).download([channel_url])

if __name__ == '__main__':
    set_args()
    if IMPORT_CONF:
        try:
            with open('ytm-channels.conf', 'r') as conf:
                for line in conf.readlines():
                    CHANNELS_LIST.append(line.strip('\n').strip(' '))
        except:
            print('Add Youtube channels to \'ytm-channels.conf\'')
            sys.exit(0)
    
    try:
        Downloader(CHANNELS_LIST).run()
    except KeyboardInterrupt:
        sys.exit(0)
