FROM arm32v7/python:3.6-buster

COPY GenerateSave.py
COPY requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "GenerateSave.py"]
