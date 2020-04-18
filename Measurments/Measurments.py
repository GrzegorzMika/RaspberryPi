import time
from datetime import datetime
from logging import debug

from grove.grove_moisture_sensor import GroveMoistureSensor
from seeed_dht import DHT


def main():
    sensor_temperature = DHT("11", 12)
    sensor_moisture = GroveMoistureSensor(0)

    with open('measurements.txt', 'w+') as f:
        f.write('Timestamp, Humidity, Temperature, Moisture\n')
    while True:
        try:
            with open('measurements.txt', 'a+') as f:
                humi, temp = sensor_temperature.read()
                mois = sensor_moisture.moisture
                now = datetime.now()
                f.write('{}, {}, {}, {}\n'.format(now.strftime("%H:%M:%S"), humi, temp, mois))
            time.sleep(15)
        except Exception as err:
            debug(err)


if __name__ == '__main__':
    main()
