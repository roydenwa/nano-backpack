FROM python:3.7

# get and install dependencies first to utilize docker-cache
RUN pip install flask==1.1.1 && \
    mkdir -p /app/static && \
    wget -c https://github.com/SAP/openui5/releases/download/1.84.0/openui5-runtime-1.84.0.zip && \
    unzip openui5-runtime-1.84.0.zip -d /app/static/openui5-runtime && \
    rm -r openui5-runtime-1.84.0.zip && \
    git clone https://github.com/aldebaran/libqi-js.git /app/static/libqi-js

COPY . /app/

WORKDIR /app

CMD [ "python", "app.py" ]
