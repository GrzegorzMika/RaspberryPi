FROM arm32v7/python:3.6-buster

RUN mkdir /home/data

COPY UploadBlob.py /home/data
COPY requirements.txt /home/data
COPY secretgc.json /home/data

WORKDIR /home/data

RUN pip install -r requirements.txt

CMD ["python", "UploadBlob.py"]
