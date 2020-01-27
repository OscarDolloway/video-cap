#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:41:32 2020

@author: oscardolloway
"""
from imports import *  
from imports import m3u8scraper  


#print(viddir)


#sitetest = http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8

URL = input ('')

print(type(URL))

StrURL = (", ".join(URL))
URLlist = list(URL.split(" "))
print(type(URLlist))


# =============================================================================
# Step one check URL, if URL is M3U8 then run capture function, else run scraper
# =============================================================================
if type(URLlist) is list:
    m3u8(URLlist)


def m3u8(URL):
    if webcheck(URL) == True:
        print('webcheck, true')
        StrURL = (", ".join(URL))
        if 'm3u8' in StrURL:
            print('link contains m3u8','beginning capture')
            single_Capture(StrURL)
        else:
            print('incorrect link type')

def multi ():        
#m3u8(URL)




     
#print(multilinks)
#URL = multilinks
#print(URL)
        


        #for i in linkset:
          #  print(i)
        #print(type(linkset))
        

#print(webcheck(URL))

#m3u8scraper(URL)

#Capture(URL)



        

