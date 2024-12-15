FROM python:3.12-slim

# install dependencies
COPY ci/telegram_bot/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 

# copy codebase
WORKDIR /src
COPY src/telegram_bot .
COPY src/pub_sub.py ./pub_sub.py

ENTRYPOINT [ "python3", "run.py" ]
