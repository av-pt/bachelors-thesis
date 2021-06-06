FROM python:3.8.7

RUN pip install pipenv;

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install

RUN pipenv run python -m nltk.downloader -d /usr/share/nltk_data brown punkt
RUN pipenv run python -m spacy download en_core_web_sm

COPY clts ./clts/
COPY main.py .
COPY converters.py .

ENTRYPOINT ["pipenv", "run", "python", "main.py"]