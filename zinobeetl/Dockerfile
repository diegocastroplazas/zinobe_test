FROM python:3
RUN mkdir -p /usr/
ADD *.py /usr/src/
ADD requirements.txt /usr/src/
WORKDIR /usr/src/
RUN pip install -r requirements.txt
RUN echo "Inicializando ETL"
CMD [ "python", "./main.py"]