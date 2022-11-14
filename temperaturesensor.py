import Adafruit_DHT
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DTH11
pin = 23
while True:
    humidity,temperature =Adafruit_DHT.read_retry(sensor , pin)
    if humidity is None and temperature is None:
        print("Failed to get reading.Try Again!")
    else:
        print("Temperature={0:0.1f}*C humidity={1:0.2f}%".format(temperature,humidity))
    time.sleep(1)

