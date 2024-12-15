FROM python:3.12-slim

# install dependencies
COPY ci/websocket_chat/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 

# copy codebase
WORKDIR /src
COPY src/websocket_chat .
COPY src/pub_sub.py ./pub_sub.py

EXPOSE 8000

ENTRYPOINT [ "python3", "api_app.py" ]
