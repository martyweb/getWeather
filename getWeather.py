import requests
import json
import argparse
from influxdb import InfluxDBClient

#--------------------------------------------------------
#Get weather information from openweather
#--------------------------------------------------------

parser = argparse.ArgumentParser(description='Gimme')
parser.add_argument('-z', '--zip', required=True, help='Zipcode to get weather')
parser.add_argument('-a', '--appid', required=True, help='Appid for openweathermap.org')
parser.add_argument('-s', '--influxdbhost', required=True, help='Influxdb host')
parser.add_argument('-P', '--influxdbport', required=True, help='Influxdb port')
parser.add_argument('-u', '--influxdbusername', required=True, help='Influxdb username')
parser.add_argument('-p', '--influxdbpass', required=True, help='Influxdb pass')
parser.add_argument('-d', '--influxdbdatabase', required=True, help='Influxdb database name')

args = parser.parse_args()

url = "https://api.openweathermap.org/data/2.5/weather?zip="+args.zip+"&APPID="+args.appid+"&units=imperial"
response = requests.request("GET", url)
json_data = json.loads(response.text)

#--------------------------------------------------------
#post data to influxdb
#--------------------------------------------------------
json_body = [
            {
                        "measurement": "main",
                                "tags": {
                                                "zip": zip,
                                                            "timezone":json_data["timezone"],
                                                                        "name":json_data["name"]
                                                                                },
                                        "fields": json_data["main"]
                                            }
            ]

client = InfluxDBClient(host=args.influxdbhost, port=args.influxdbport, username=args.influxdbusername, password=args.influxdbpass,database=args.influxdbdatabase)
response = client.write_points(json_body)

print(response)
