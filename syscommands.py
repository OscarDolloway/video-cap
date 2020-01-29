#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:29:54 2020

@author: oscardolloway
"""


import os
import sys


directory = (os.path.abspath(os.path.dirname(sys.argv[0])))

ffmpeg = directory + '/bin/ffmpeg'
ffprobe = directory + '/bin/ffprobe'
command1 = [ffprobe,'http://www.bokowsky.net/de/knowledge-base/video/hls_bunny/7ea96983ed10dc5546f8275871a38df7_127912_60594786.m3u8']


os.system('ffmpeg')

os.system('ffprobe')

os.system ('ffprobe Test.mp4')

#cmd = [ffmpeg] + '-codecs'

#os.system(ffprobe+'http://www.bokowsky.net/de/knowledge-base/video/hls_bunny/7ea96983ed10dc5546f8275871a38df7_127912_60594786.m3u8')
