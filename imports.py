#!/bin/sh
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
from subprocess import run
from subprocess import Popen
from subprocess import check_output
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
print(viddir)
FFMPEG_BIN = viddir + '/ffmpeglib/bin/ffmpeg'#binary files, allows us to use the module
ffprobe = viddir + '/ffmpeglib/bin/ffprobe'


linkset =''
linkset = set()

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
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} # for when a site cant be accessed

#URL = ['http://xmtvplayer.com/snippet/sample-m3u-file']

#URL = input ('Enter site: ')
#StrURL = (", ".join(URL))



def m3u8scraper(URL):
    req = Request(URL,headers=user_agent)
    site = urlopen(req).read()
    try:
        page = urlopen(req)
    except:
        print('site not valid')
        sys.exit()
    response = get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    #content =  soup.find_all("p", {"class": "box"},"")
    All = soup.text#All containers from the site
    #print(type(All))
    links = re.findall("(?P<element>[\w\.\/\-\\:]+\.m3u8)",All)#regex to capture m3u8 links
    if not links:
        print("no m3u8s found")
        return False
    else:
        print('m3u8s Found/n')
        
        #linkset = set(links) # added as a set to remove duplicates
        for i in links:
            print(i + '\n')
            linkset.add(i)
        print(linkset)
            #multilinks.append(i)
        return True
        
#m3u8scraper(StrURL)
m3u8URL = ['http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8','www.bad.cesf',
           'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8']
def Capture(URL):
    #linkset = [linkset]
    cap_dur = 5
    cap_num = 1
    print(cap_num)
    for urls in range(len(URL)):
        print(URL[urls])
        
        
        cap = cv2.VideoCapture(URL[urls])
        if (cap.isOpened()==True):
        
            cmd = [ffprobe] +' -show_format -show_streams -loglevel quiet -print_format json'.split() + [URL[urls]]
            metadata = sp.check_output(cmd).decode('utf-8')
            print(metadata)
        
        
            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)# gets the correct height&width of live vid
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')#video type
            out = cv2.VideoWriter((str(cap_num)+'.mp4'),fourcc,24,(int(width),int(height)))
            cap_num = cap_num +1#stores us to store new videos
            print(cap_num)
            start_time = time.time()
            while (int(time.time() - start_time)<cap_dur):
                ret, frame = cap.read()
                if ret == True:
                    frame = cv2.flip(frame,180)# allows us to store the video, without only 1 frames stores
                    out.write(cv2.flip(frame, 180))#flips and flips again to get correct frame
                else:
                    break
        else:
            
            cap.release()
            out.release()
            cv2.destroyAllWindows()
    
#Capture(m3u8URL)
def single_Capture(URL):
    vidname = (str(URL))
    cap_dur = 10
    print(URL)
    cap = cv2.VideoCapture(URL)
    
    cmd = [ffprobe] +' -show_format -show_streams -loglevel quiet -print_format json'.split() + [URL]
    print(cmd)
    metadata = sp.check_output(cmd).decode('utf-8')
    
    print(metadata)
    pipe = sp.Popen([ FFMPEG_BIN, "-i", URL,
                     '-ss', '0', '-t', '120'
            # no text output
               # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-r",'1',
           "-vcodec", "rawvideo", "-"],shell=False,
           stdin = sp.PIPE, stdout = sp.PIPE)
    
    framecount = cap.get(cv2.CAP_PROP_FRAME_COUNT ) 
    frames_per_sec = cap.get(cv2.CAP_PROP_FPS)
    
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)# gets the correct height&width of live vid
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')#video type
    
    out = cv2.VideoWriter (('Test.mp4'),fourcc,24,(int(width),int(height)))
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
    