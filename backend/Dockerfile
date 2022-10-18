FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python -m pip install --upgrade pip

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]