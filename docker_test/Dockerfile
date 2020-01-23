FROM arm32v7/python:3.6-buster

RUN mkdir /home/data

COPY GenerateSave.py /home/data
COPY requirements.txt /home/data

WORKDIR /home/data

RUN pip install -r ./requirements.txt

CMD ["python", "./GenerateSave.py"]
