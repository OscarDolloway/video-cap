#getting base image
#!/usr/bin/env python3
FROM ubuntu:16.04
FROM python

MAINTAINER oscar dolloway <oscar.dolloway@hotmail.co.uk>

RUN mkdir video_cap


#RUN apt-get update
RUN apt-get install -y git
#RUN apt install python3-pip
RUN pip install scipy
RUN pip install numpy
RUN pip install matplotlib
RUN pip install BeautifulSoup4
RUN pip install requests
RUN pip install subprocess.run
#RUN pip install ffmpeg
#RUN pip install opencv
RUN pip install opencv-python


RUN apt-get update
#RUN apt-get install ffmpeg
RUN apt-get -y install ffmpeg

RUN git clone https://github.com/OscarDolloway/video-cap.git video_cap 
#COPY /Users/odolloway/Documents/GitHub/video-cap/ video_cap

#RUN ls -la /video_cap/Test.mp4

RUN chmod 644 /video_cap
RUN ls -la /video_cap/
RUN ls /video_cap

CMD ffmpeg

#CMD find video_cap -name 'test.mp4'
CMD python video_cap/m3u8capture.py


#CMD ls -la /video_cap/


