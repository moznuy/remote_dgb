FROM python:3.7-alpine

COPY main.py /app/

WORKDIR /app
#RUN pip install
CMD python -u main.py
