#!/usr/bin/python3

# run this by cron:
# crontab -l
# 1,11,21,31,41,51 * * * * python3 /home/pi/AQDbridge/purpleaqd-get-once.py

import re
from typing import NamedTuple
import time
import requests
from influxdb import InfluxDBClient

INFLUXDB_ADDRESS = 'localhost'
INFLUXDB_USER = 'purpleguy'
INFLUXDB_PASSWORD = 'passwordsuperstrong'
INFLUXDB_DATABASE = 'weather_stations'

PURPLE_URL = 'http://192.168.0.164/json'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)


def send_sensor_data_to_influxdb(sensor_data):
    json_body = [
        {
            'measurement': 'PurpleAirQuality',
            'tags': {
                'location': 'RockyPoint'
            },
            'fields': #{
                sensor_data
#                'value': sensor_data.value
            #}
        }
    ]
#    print (json_body)
    influxdb_client.write_points(json_body)


def _init_influxdb_database():
    databases = influxdb_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)

def main():
    _init_influxdb_database()

    r_json = requests.get(PURPLE_URL)
    if r_json.status_code == 200:
        send_sensor_data_to_influxdb(r_json.json())

if __name__ == '__main__':
#    print('PurpleAQD to InfluxDB bridge')
    main()
