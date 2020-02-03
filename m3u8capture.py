#!/bin/sh

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:41:32 2020

@author: oscardolloway
"""
#print(viddir)
from imports import *


#URL = 'http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8'
print('----- Enter site for capture:')
URL = input ('---- : ')
print('\n')

#StrURL = (", ".join(URL))
URLlist = list(URL.split(" "))
#print(type(URLlist))


# =============================================================================
# check URL status
# =============================================================================
# check what URL m3u8 or HTML
# =============================================================================
#           if m3u8, attempt a capture
#       else
#            attempt a scrape of links from the site
#scrape the multiple links
# =============================================================================

def m3u8(URL):
    if webcheck(URL) == True:
        print('---- Webcheck complete, site is online'+ '\n')
        StrURL = (", ".join(URL))
        if 'm3u8' in StrURL:
            print('link contains m3u8','beginning stream capture')
            single_Capture(StrURL)
        else:
            print('---- Does not contain m3u8, running web scraper')
            if m3u8scraper(StrURL) == True:
                pass
                #not quite ready
                #Capture(linkset)
if type(URLlist) is list:
    m3u8(URLlist)

        

