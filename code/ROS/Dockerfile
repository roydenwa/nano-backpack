# src: https://hub.docker.com/r/ct2034/vnc-ros-kinetic-full/dockerfile
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

# built-in packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common curl \
    && sh -c "echo 'deb http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >> /etc/apt/sources.list.d/arc-theme.list" \
    && curl -SL http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key | apt-key add - \
    && add-apt-repository ppa:fcwu-tw/ppa \
    && apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated \
        supervisor \
        openssh-server pwgen sudo vim-tiny \
        net-tools \
        lxde x11vnc xvfb \
        gtk2-engines-murrine ttf-ubuntu-font-family \
        firefox \
        nginx \
        python-pip python-dev build-essential \
        mesa-utils libgl1-mesa-dri \
        gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme \
        dbus-x11 x11-utils \
        terminator \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# install ros (source: https://github.com/osrf/docker_images/blob/5399f380af0a7735405a4b6a07c6c40b867563bd/ros/kinetic/ubuntu/xenial/ros-core/Dockerfile)
# install packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    dirmngr \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# setup keys
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    && rm -rf /var/lib/apt/lists/*

# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# bootstrap rosdep
RUN rosdep init \
    && rosdep update

# install ros packages
ENV ROS_DISTRO kinetic
RUN apt-get update && apt-get install -y \
#    ros-kinetic-ros-core=1.3.1-0* \
    ros-kinetic-desktop-full \
    && rm -rf /var/lib/apt/lists/*

# user tools
RUN apt-get update && apt-get install -y \
    terminator \
    gedit \
    okular \
    vim \
    && rm -rf /var/lib/apt/lists/*

# tini for subreap
ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
RUN chmod +x /bin/tini

ADD image /
RUN pip install setuptools wheel && pip install -r /usr/lib/web/requirements.txt

# install Python 3.7
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
    apt-get install -y curl python3.7 python3.7-dev python3.7-distutils

# install NAOqi
RUN mkdir ~/naoqi && apt-get install -y wget && \
    wget "https://community-static.aldebaran.com/resources/2.8.5/naoqi-sdk-2.8.5.10-linux64.tar.gz" -P ~/naoqi && \
    wget "https://community-static.aldebaran.com/resources/2.8.6/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327.tar.gz" -P ~/naoqi && \
    tar xzf ~/naoqi/naoqi-sdk-2.8.5.10-linux64.tar.gz -C ~/naoqi && \
    tar xzf ~/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327.tar.gz -C ~/naoqi && \
    rm ~/naoqi/naoqi-sdk-2.8.5.10-linux64.tar.gz && rm ~/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327.tar.gz

RUN cp /usr/share/applications/terminator.desktop /root/Desktop
RUN echo "source /opt/ros/kinetic/setup.bash" >> /root/.bashrc

# add NAOqi paths to .bashrc
RUN echo "export PYTHONPATH=~/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327:$PYTHONPATH" >> /root/.bashrc && \
    echo "export AL_DIR=~/naoqi/naoqi-sdk-2.8.5.10-linux64" >> /root/.bashrc && \
    echo "export AL_DIR_SIM=~/naoqi/naoqi-sdk-2.8.5.10-linux64" >> /root/.bashrc && \
    echo "export PYTHONPATH=~/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib/python2.7/site-packages:$PYTHONPATH" >> /root/.bashrc && \
    echo "export QI_SDK_PREFIX=~/naoqi/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327" >> /root/.bashrc

# install needed pkgs and NAO pkg for ROS kinetic
RUN apt-get install -y ros-kinetic-driver-base ros-kinetic-move-base-msgs \
    ros-kinetic-octomap ros-kinetic-octomap-msgs ros-kinetic-humanoid-msgs \
    ros-kinetic-humanoid-nav-msgs ros-kinetic-camera-info-manager \
    #os-kinetic-camera-info-manager-py \
    ros-kinetic-nao-robot

# install pkgs to control NAO
RUN apt-get install -y ros-kinetic-nao-bringup ros-kinetic-naoqi-pose \
    ros-kinetic-nao-interaction ros-kinetic-nao-moveit-config \
    ros-kinetic-naoqi-driver ros-kinetic-naoqi-driver-py \
    ros-kinetic-naoqi-sensors-py ros-kinetic-nao-dcm-bringup \
    ros-kinetic-moveit

EXPOSE 80
WORKDIR /root
ENV HOME=/home/ubuntu \
    SHELL=/bin/bash
ENTRYPOINT ["/startup.sh"]
