import time
from seeed_dht import DHT
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.display.jhd1802 import JHD1802


def main():
    sensor_moist = GroveMoistureSensor(0)
    sensor_tmp = DHT("11", 12)
    lcd = JHD1802()

    lcd.home()
    lcd.write("LCD model:".format(lcd.name))
    lcd.setCursor(1, 0)
    lcd.write("{}".format(lcd.name))
    time.sleep(5)
    lcd.clear()

    while True:
        for i in range(10):
            humi, temp = sensor_tmp.read()
            lcd.setCursor(0, 0)
            lcd.write('Temp.: {0:.1f}C'.format(temp))
            lcd.setCursor(1, 0)
            lcd.write('Humi.: {0:.1f}%'.format(humi))
            time.sleep(5)
            # lcd.clear()
        lcd.clear()
        mois = sensor_moist.moisture
        lcd.setCursor(0, 0)
        lcd.write('moisture: {0:>6}'.format(mois))
        time.sleep(5)
        lcd.clear()


if __name__ == '__main__':
    main()
