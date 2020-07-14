# getWeather
Get weather from openweathermap.org using a zip code and then send data to influxdb

# Build
git clone https://github.com/martyweb/getWeather.git
cd getWeather
sudo docker build -t getweather .

# Run
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
