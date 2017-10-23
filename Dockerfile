FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
MAINTAINER Coldsheep <coldsheep@ailabs.tw>

# Setup environment variables
ENV JIEBA_DATA=/root/data/extra_dict \
    DATA=/root/data/data \
    POSTS=/root/_posts \
    TEMPLATE=/root/data/news-templates \
    DOC=/root/data/drqa_data/db.db \
    READER=/root/model/20170818-18a0e71b.mdl \
    TFIDF_DATA=/root/data/drqa_data/tfidf.npz \
    PYTHONPATH=/root/DrQA:$PYTHONPATH \
    DBDATA=/root/data/ptt_data \
    TZ=Asia/Taipei

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata \
 && echo $TZ | tee /etc/timezone \
 && rm /etc/localtime \
 && dpkg-reconfigure --frontend noninteractive tzdata

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
            python-dev \
            python3.5


COPY requirements.txt /root/
RUN apt-get install -y python3-pip \
 && pip3 install http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp35-cp35m-manylinux1_x86_64.whl \
 && pip3 install -r /root/requirements.txt

COPY util /root/util
COPY DrQA /root/DrQA
COPY lists /root/lists
COPY journalist.py /root/

WORKDIR /root
CMD python3 journalist.py
