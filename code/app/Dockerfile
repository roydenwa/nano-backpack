FROM python:3.7

COPY . /app/

RUN pip install flask==1.1.1 && \
    wget -c https://github.com/SAP/openui5/releases/download/1.84.0/openui5-runtime-1.84.0.zip && \
    unzip openui5-runtime-1.84.0.zip -d /app/static/openui5-runtime && \
    rm -r openui5-runtime-1.84.0.zip

WORKDIR /app

CMD [ "python", "app.py" ]
