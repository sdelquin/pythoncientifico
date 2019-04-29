FROM python:3.6
LABEL Maintainer="Sergio Delgado Quintero <sdelquin@gmail.com>"

RUN pip install pipenv

COPY . /pythoncientifico

WORKDIR /pythoncientifico
RUN pipenv install

CMD pipenv run jupyter notebook --ip=0.0.0.0 --port=8080 --allow-root --NotebookApp.token=''
