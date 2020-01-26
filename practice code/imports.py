#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:42:08 2020

@author: oscardolloway
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.image as mpimg
from matplotlib.pyplot import figure, imshow, axis
import cv2
import sys
import subprocess as sp
from threading import Timer
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
from requests import get
import numpy as np
import re
import requests
import urllib.request
from requests.exceptions import HTTPError
import time

viddir = (os.path.dirname(os.path.abspath(sys.argv[0])))#current directory
FFMPEG_BIN = viddir + '/ffmpeglib/bin/ffmpeg'
ffprobe = viddir + '/ffmpeglib/bin/ffprobe'

multilinks = []

def webcheck (URL):
    for urls in URL:
        try:
            response = requests.get(urls)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            return True
#webcheck(multilinks)   
#URL = "http://xmtvplayer.com/snippet/sample-m3u-file"
#import urllib2
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} # for when a site cant be accessed

def m3u8scraper(URL):
    req = Request(URL,headers=hdr)
    site = urlopen(req).read()
    try:
        page = urlopen(req)
    except:
        print('site not valid')
        sys.exit()
    response = get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    #content =  soup.find_all("p", {"class": "box"},"")
    All = soup.text
    #print(type(All))
    links = re.findall("(?P<element>[\w\.\/\-\\:]+\.m3u8)",All)
    linkset = set(links)
    for i in linkset:
        print(i)
        multilinks.append(i)
    return linkset
#m3u8scraper(URL)

def Capture(multilinks):
    cap_dur = 5
    cap_num = 1
    print(cap_num)
    for urls in range(len(URL)):
        print(URL[urls])
        #cmd = [ffprobe] + '-show_format -pretty -loglevel quiet'.split()+[URL[urls]]
        #ffout = sp.check_output(cmd).decode('utf-8')
        #print(ffout)
        cap = cv2.VideoCapture(URL[urls])
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)# gets the correct height&width of live vid
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')#video type
        out = cv2.VideoWriter((str(cap_num)+'.mp4'),fourcc,24,(int(width),int(height)))
        cap_num = cap_num +1#stores us to store new videos
        start_time = time.time()
        while (int(time.time() - start_time)<cap_dur):
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.flip(frame,180)# allows us to store the video, without only 1 frames stores
                out.write(cv2.flip(frame, 180))
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    
#Capture(multilinks)
def single_Capture(URL):
    cap_dur = 60
    print(URL)
    cap = cv2.VideoCapture(URL)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)# gets the correct height&width of live vid
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')#video type
    
    out = cv2.VideoWriter ('Test.mp4',fourcc,24,(int(width),int(height)))
    start_time = time.time()
    while (int(time.time() - start_time)<cap_dur):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame,180)# allows us to store the video, without only 1 frames stores
            out.write(cv2.flip(frame, 180))
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    