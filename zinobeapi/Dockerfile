FROM python:3
ADD *.py /usr/src/
ADD requirements.txt /usr/src/
WORKDIR /usr/src/
RUN pip install -r requirements.txt
RUN echo "Inicializando API...."
CMD [ "python", "./app.py"]