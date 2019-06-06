# Based on 18.04 LTS
# for gamera framework 
FROM ubuntu

RUN apt-get upgrade && \
apt-get update && \
apt-get install -y \
python3-pip \
python-pip \
gcc \
libtiff5 \
libpng12-0 \
  && \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro && \ 
  -e DISPLAY=$DISPLAY 



# indented lines from https://groups.google.com/forum/#!topic/etetoolkit/4SrZk5fRtCM
#WORKDIR /root
#More info on graphics inside docker:
#https://stackoverflow.com/questions/25281992/alternatives-to-ssh-x11-forwarding-for-docker-containers/25334301#25334301


CMD ["bash"]
