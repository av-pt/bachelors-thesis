FROM python:3.9.0

RUN pip install pipenv;

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install

RUN pipenv run python -m nltk.downloader -d /usr/share/nltk_data brown

COPY main.py .

ENTRYPOINT ["pipenv", "run", "python", "main.py"]