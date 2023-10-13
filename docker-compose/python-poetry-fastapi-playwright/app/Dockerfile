FROM ubuntu:latest
RUN apt-get update -y && apt-get install curl -y && apt-get install python3-pip -y
# RUN apt-get install libzbar0 -y && apt-get install tesseract-ocr -y && apt-get install libtesseract-dev -y
# RUN apt-get -y install poppler-utils
RUN pip install pytest-playwright && playwright install && playwright install-deps
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH="${PATH}:/etc/poetry/bin:$PATH"
WORKDIR "/app"
ADD . .
RUN poetry install
EXPOSE 8080
ENTRYPOINT ["poetry","run","prod"]