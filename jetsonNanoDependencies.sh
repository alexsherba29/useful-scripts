#!/bin/bash

sudo jetson_clocks
sudo apt update
sudo apt install -y build-essential make cmake cmake-curses-gui \
                      git g++ pkg-config curl libfreetype6-dev \
                      libcanberra-gtk-module libcanberra-gtk3-module \
                      python3-dev python3-pip
sudo pip3 install -U pip==21.1.2 Cython testresources setuptools
sudo pip3 install numpy==1.20.3 matplotlib==3.4.2
