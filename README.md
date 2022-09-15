# Youtube-Music-Downloader

Download music from your favourite Youtube channels!

# Requirements:
- youtube-dl: ```pip install youtube-dl```
- ffmpeg: ```pip install ffmpeg```
- BeautifulSoup: ```pip install BeautifulSoup4```

# Usage: 
  Add your Youtube channels to 'ytm-channels.conf' file
```bash
usage: ytm [-h] [-n [NUMBER]] [-a] [-u USER]

Youtube music downloader

optional arguments:
  -h, --help            show this help message and exit
  -n [NUMBER], --number [NUMBER]
                        Number of music per channel [1-30]
  -a, --auto            Automatically download new music that are not already
                        downloaded
  -u USER, --user USER  Download music from a specified user
```

# Command Line Example:
    $ python ytm -a
    $ python ytm -a -n 10
    $ python ytm -u AllTrapNation -n 10
