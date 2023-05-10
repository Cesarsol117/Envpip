FROM python:3.8 
WORKDIR /csv
COPY requirements.txt /csv/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /csv/requirements.txt

COPY . /csv/

CMD bash -c "while true; do sleep1; done"