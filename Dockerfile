FROM python:3
ENV zip=0
ENV appid=""
ENV influxdbhost=""
ENV influxdbport=""
ENV influxdbusername=""
ENV influxdbpass=""
ENV influxdbdatabase=""

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./getWeather.py", "--zip", $zip, "--appid", $appid, "--influxdbhost", $influxdbhost, "--influxdbport", $influxdbport, "--influxdbusername", $influxdbusername, "--influxdbpass", $influxdbpass, "--influxdbdatabase", $influxdbdatabase  ]
