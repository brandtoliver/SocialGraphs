#FROM python:3.6-alpine

#RUN mkdir /app
#WORKDIR /app
#ADD requirements.txt /app/

#RUN pip install -r requirements.txt
#ADD . /app/

#ENTRYPOINT [ "python" ]
#CMD ["app.py"]



FROM tiangolo/uwsgi-nginx-flask:python3.6

#RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/

RUN pip install -U pip && pip install -r requirements.txt
ADD . /app/

#ENV NGINX_WORKER_PROCESSES auto

ENTRYPOINT [ "python" ]
CMD ["index.py"]
