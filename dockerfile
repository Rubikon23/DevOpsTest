FROM python:3.7-alpine
ADD . /devtest
WORKDIR /devtest
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code
RUN echo '*/1 * * * * python /code/sender.py; /bin/sleep 15; python /code/sender.py; /bin/sleep 15; python /code/sender.py; /bin/sleep 15; python /code/sender.py' >> /etc/crontabs/root
CMD  crond -b && python app.py

