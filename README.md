# Bachelors Thesis: Authorship Identification using phonological features
## Notes
This project uses Docker and Pipenv. [Git-flow](https://danielkummer.github.io/git-flow-cheatsheet/) is used for a clean branching structure. Install Docker ([Linux](https://docs.docker.com/install/), [MacOS](https://docs.docker.com/docker-for-mac/install/), [Windows](https://docs.docker.com/docker-for-windows/install/)) following the official documentation!

## Getting Started
Python 3.8 needs to be installed.
Run `pipenv install` in the base folder to create an environment with all necessary dependencies.
Run `pipenv run python -i converters.py` to load the converters script and start an interactive console.
Then try `g2p('Some text.', 'soundex')` or `g2sc('Some text.', 'dolgo')` to convert text.

#### Outdated
~~Common actions are wrapped in a Makefile for easier access.~~
~~1. Build container: `make build`~~
~~2. Run container: `make run`~~
