# Based on 18.04 LTS
# for gamera framework 
FROM ubuntu

RUN apt-get upgrade && \
apt-get update

RUN apt-get install -y \
python3-pip \
python-pip 

RUN apt-get install -y git \
wget \
cmake \
ninja-build \
pkg-config \
libgtk-3-dev

RUN apt-get install -y libpng-dev  

#install gkt+ [wget dependency]



#install wget [gamera GUI dependency]
RUN wget -O \
wxPython-src-3.0.1.1.tar.bz2 \
https://sourceforge.net/projects/wxpython/files/wxPython/3.0.1.1/wxPython-src-3.0.1.1.tar.bz2/download \ &&

tar -xjf wxPython-src-3.0.1.1.tar.bz2 \ &&

cd wxPython-src-3.0.1.1 \ &&

python build-wxpython.py --build_dir=../bld


#install libtiff
RUN wget http://download.osgeo.org/libtiff/tiff-4.0.10.tar.gz && \
tar -xzf tiff-4.0.10.tar.gz && \
cd tiff-4.0.10 && \
mkdir libtiff-build && \
cd libtiff-build && \
cmake -DCMAKE_INSTALL_DOCDIR=/usr/share/doc/libtiff-4.0.10 \
      -DCMAKE_INSTALL_PREFIX=/usr -G Ninja .. && \
ninja && \
ninja install && \
rm ../../tiff-4.0.10.tar.gz


#install gamera

RUN git clone https://github.com/hsnr-gamera/gamera.git gamera-src && \
cd gamera-src 
# && \
#python setup.py build && \
#sudo python setup.py install

#RUN apt-get install -y python3-matplotlib
#RUN apt-get install libtiff5 


# indented lines from https://groups.google.com/forum/#!topic/etetoolkit/4SrZk5fRtCM
#WORKDIR /root
#More info on graphics inside docker:
#https://stackoverflow.com/questions/25281992/alternatives-to-ssh-x11-forwarding-for-docker-containers/25334301#25334301


CMD ["bash"]
