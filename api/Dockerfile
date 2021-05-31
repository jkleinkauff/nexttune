FROM python:3.6-slim-stretch
RUN pip install --upgrade pip

COPY . /usr/src/api

ENV PYTHONPATH "."
ENV FLASK_APP "main.py"
WORKDIR /usr/src/api

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --requirement requirements.txt

# CMD ["python", "main.py"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]