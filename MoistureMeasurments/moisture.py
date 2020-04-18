#!/usr/bin/env python
import time
from datetime import datetime
import logging

from grove.grove_moisture_sensor import GroveMoistureSensor

logging.basicConfig(filename='./log.log', level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


def main():
    period = 60
    wait = 59.99/period
    sensor = GroveMoistureSensor(0)

    with open('moisture_2.txt', 'w+') as f:
        f.write('Timestamp, Moisture\n')

    while True:
        moisture_temporary = []
        for _ in range(period):
            try:
                moisture_temporary.append(sensor.moisture)
            except Exception as e:
                logging.error(e)
            finally:
                time.sleep(wait)
        moisture = sum(moisture_temporary) / len(moisture_temporary)
        now = datetime.now()
        with open('moisture_2.txt', 'a+') as f:
            try:
                # print('Measurement: {}'.format(moisture))
                f.write('{}, {}\n'.format(now.strftime("%Y-%m-%d %H:%M:%S"), moisture))
            except Exception as e:
                logging.error(e)


if __name__ == '__main__':
    main()
