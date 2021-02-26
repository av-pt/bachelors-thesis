FROM python:3.8.7

RUN pip install pipenv;

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install

RUN pipenv run python -m nltk.downloader -d /usr/share/nltk_data brown punkt

COPY clts ./clts/
COPY main.py .
COPY converters.py .

ENTRYPOINT ["pipenv", "run", "python", "main.py"]