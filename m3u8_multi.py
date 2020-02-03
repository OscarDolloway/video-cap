#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:02:00 2020

@author: oscardolloway
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.image as mpimg
from matplotlib.pyplot import figure, imshow, axis
import cv2
import subprocess as sp
from subprocess import run
from subprocess import Popen
from subprocess import check_output
from threading import Timer
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import requests
from requests import get
import re
#import ffmpeg
import urllib.request
from requests.exceptions import HTTPError
import time

viddir = (os.path.abspath(os.path.dirname(sys.argv[0])))#current directory
URL = ['http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8',
           'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8']




def Capture(URL):
    #linkset = [linkset]
    cap_dur = 5
    cap_num = 1
    #print(cap_num)
    for urls in range(len(URL)):
        print('---- URL: ----')
        print(URL[urls]+ '\n')
        
        print('---- live meta: ----')
        
        os.system ('ffmpeg -i ' +' '+URL[urls])
        
        cap = cv2.VideoCapture(URL[urls])
        if (cap.isOpened()==True):
            
            
            #Meta:
            #cmd = [ffprobe] +' -show_format -show_streams -loglevel quiet -print_format json'.split() + [URL[urls]]
            #metadata = sp.check_output(cmd).decode('utf-8')
            #print(metadata)
            
            
            
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
                    #print(viddir)
                else:
                    
                    break
        else:
           
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            viddir = (os.path.abspath(os.path.dirname(sys.argv[0])))#current directory
            print(viddir)
    
Capture(URL)
files = os.listdir(viddir)
print(files)