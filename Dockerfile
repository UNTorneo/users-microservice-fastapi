FROM python:3.11

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install psycopg2
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install sqlalchemy

COPY ./app /code/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]