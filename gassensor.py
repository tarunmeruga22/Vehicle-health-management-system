import time.sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

def action(pin):

    print("sensor detected action")
    return

GPIO.add_event_detect(35, GPIO.RISING)

GPIO.add_event_callback(35, action)

try:

    while True:

          print("Alive") 
          time.sleep(0.5)

except KeyboardInterrupt:
      GPIO.cleanup()
      sys.exit() 