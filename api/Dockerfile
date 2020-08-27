FROM python:3-onbuild  

COPY . /usr/src/api

ENV PYTHONPATH "."
ENV FLASK_APP "main.py"
EXPOSE 5000
WORKDIR /usr/src/api
# CMD ["python", "main.py"]

CMD ["flask", "run", "--host=0.0.0.0"]