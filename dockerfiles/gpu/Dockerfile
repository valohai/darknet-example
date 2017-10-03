FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

MAINTAINER Ruksi <ruksi@valohai.com>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 CUDA_ROOT="/usr/local/cuda/bin"

RUN apt-get update --fix-missing && \
    apt-get install -y \
        libopencv-dev \
        python-opencv \
        git \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/pjreddie/darknet.git /darknet
WORKDIR /darknet
RUN sed -i'' -- 's/GPU=0/GPU=1/g' Makefile
RUN sed -i'' -- 's/CUDNN=0/CUDNN=1/g' Makefile
RUN make

ENTRYPOINT []
CMD ["/bin/bash"]
