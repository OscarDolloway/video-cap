#!/bin/sh

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:41:32 2020

@author: oscardolloway
"""
from imports import *


#print(viddir)


#URL = 'http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8'

URL = input ('Enter site: ')


StrURL = (", ".join(URL))
URLlist = list(URL.split(" "))
print(type(URLlist))


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
        print('webcheck, site up')
        StrURL = (", ".join(URL))
        if 'm3u8' in StrURL:
            print('link contains m3u8','beginning stream capture')
            single_Capture(StrURL)
        else:
            print('working site but not .m3u8, running web scraper..')
            if m3u8scraper(StrURL) == True:
                pass
                #not quite ready
                #Capture(linkset)
if type(URLlist) is list:
    m3u8(URLlist)

     
#print(multilinks)
#URL = multilinks
#print(URL)
        


        #for i in linkset:
          #  print(i)
        #print(type(linkset))
        

#print(webcheck(URL))

#m3u8scraper(URL)

#Capture(URL)



        

