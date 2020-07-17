# getWeather
Get weather data from [openweathermap.org](http://www.openweathermap.org) using a zipcode and then send data to influxdb

# Build
```bash
git clone https://github.com/martyweb/getWeather.git
cd getWeather
sudo docker build -t getweather .
```

# Run

```bash
docker run  \
--name getWeather \
-e zip=<zipcode> \
-e appid="<id from openweathermap.org>" \
-e influxdbhost="<ip>" \
-e influxdbport="8086" \
-e influxdbusername="weather" \
-e influxdbpass="<password>" \
-e influxdbdatabase="weather" \
getweather
```