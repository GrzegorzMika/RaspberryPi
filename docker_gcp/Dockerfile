FROM python:3.6

RUN mkdir /home/data

COPY UploadBlob.py /home/data
COPY requirements.txt /home/data
COPY secretgc.json /home/data

WORKDIR /home/data

RUN pip install -r requirements.txt

CMD ["python", "UploadBlob.py"]
