FROM python:3.8.14-slim

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV MONGO_URI=mongodb://localhost:27017/
ENV MARIA_HOST=localhost

ENTRYPOINT [ "python", "mongo_handler.py" ]