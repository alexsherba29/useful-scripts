#!/bin/bash

sudo jetson_clocks
sudo add-apt-repository universe
sudo add-apt-repository multiverse

sudo apt update
sudo apt install -y build-essential make cmake cmake-curses-gui \
                      git g++ pkg-config curl libfreetype6-dev \
                      libcanberra-gtk-module libcanberra-gtk3-module \
                      python3-dev python3-pip
sudo pip3 install -U pip==21.1.2 Cython testresources setuptools
sudo pip3 install numpy==1.20.3 matplotlib==3.4.2

sudo apt install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev \
                      zip libjpeg8-dev liblapack-dev libblas-dev gfortran
                      

sudo apt-get install gstreamer1.0-tools gstreamer1.0-alsa \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
  gstreamer1.0-libav
sudo apt-get install libgstreamer1.0-dev \
  libgstreamer-plugins-base1.0-dev \
  libgstreamer-plugins-good1.0-dev \
  libgstreamer-plugins-bad1.0-dev


