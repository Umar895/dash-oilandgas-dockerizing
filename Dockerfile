FROM python:3.6-slim-jessie

COPY . /src

WORKDIR /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN python3 app.py

EXPOSE 5000
CMD ["python3", "app.py"]
