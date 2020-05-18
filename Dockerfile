FROM python:3

ADD . /www
WORKDIR /www

RUN python -m pip install --upgrade pip 
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

CMD uwsgi uwsgi.ini