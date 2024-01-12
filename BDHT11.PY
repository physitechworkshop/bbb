#pip3 install adafruit-circuitpython-dht
#sudo apt-get install libgpiod2
import Adafruit_DHT
from time import sleep

# Sensor type - DHT11
sensor = Adafruit_DHT.DHT11

# The GPIO pin number where the sensor is connected (using P8_11 as an example)
gpio_pin = 'P8_11'

while True:
    # Reading from DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

    # Checking if reading was successful
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
    else:
        print('Failed to get reading. Try again!')

    # Sleep for a bit before the next reading
    sleep(2)