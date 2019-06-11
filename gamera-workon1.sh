#!/bin/sh
#Xquartz must be open for GUI to work
#instructions at https://sourabhbajaj.com/blog/2017/02/07/gui-applications-docker-mac/

#When running for first time or if changes are made to Dockerfile,
#uncomment the following code
#
docker build -t gamera-image .
#
#get IP address
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')

docker run -it --rm \
-e DISPLAY=unix$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
-v ~/Desktop/MusicApp:/home/MusicApp \
--name="gamera-container" gamera-image

