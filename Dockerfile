From python:3.6
WORKDIR /Project/demo

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python","server.py"]