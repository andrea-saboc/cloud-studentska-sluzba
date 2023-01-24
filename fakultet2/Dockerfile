FROM python:3.10

WORKDIR /app

COPY ./fakultet2 .

RUN pip install -r requirements.txt

EXPOSE 8002

CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8002

#RUN chmod +x /app/skripta.sh

#ENTRYPOINT [ "/app/skripta.sh" ]
