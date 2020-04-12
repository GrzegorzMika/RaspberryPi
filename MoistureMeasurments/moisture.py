#!/usr/bin/env python

import time

from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.display.jhd1802 import JHD1802


def main():
    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    # Grove - Moisture Sensor connected to port A0
    sensor = GroveMoistureSensor(0)

    lcd.home()
    lcd.write("LCD model:".format(lcd.name))
    lcd.setCursor(1, 0)
    lcd.write("{}".format(lcd.name))
    time.sleep(5)
    lcd.clear()

    while True:
        mois = sensor.moisture
        if 0 <= mois < 300:
            level = 'dry'
        elif 300 <= mois < 600:
            level = 'moist'
        else:
            level = 'wet'

        for i in range(16):
            lcd.setCursor(0, 0)
            lcd.write('moisture: {0:>6}'.format(mois))
            lcd.setCursor(1, i)
            lcd.write('{}'.format(level))
            time.sleep(1)
            lcd.clear()


if __name__ == '__main__':
    main()
