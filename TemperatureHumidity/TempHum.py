import time
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802


def main():
    sensor = DHT("11", 12)
    lcd = JHD1802()

    lcd.home()
    lcd.write("LCD model:".format(lcd.name))
    lcd.setCursor(1, 0)
    lcd.write("{}".format(lcd.name))
    time.sleep(5)
    lcd.clear()

    while True:
        humidity = []
        temperature = []

        for _ in range(60*60):
            humi, temp = sensor.read()
            humidity.append(humi)
            temperature.append(temp)
            lcd.setCursor(0, 0)
            lcd.write('Temp.: {}C'.format(temp))
            lcd.setCursor(1, 0)
            lcd.write('Humi.: {}%'.format(humi))
            time.sleep(1)
        lcd.clear()
        temp_avg = round(sum(temperature)/len(temperature), 1)
        hum_avg = round(sum(humidity)/len(humidity), 1)
        lcd.setCursor(0, 0)
        lcd.write('Avg. temp.: {0:.1f}C'.format(temp_avg))
        lcd.setCursor(1, 0)
        lcd.write('Avg. humi.: {0:.1f}%'.format(hum_avg))
        time.sleep(20)
        lcd.clear()


if __name__ == '__main__':
    main()
