import RPi.GPIO as GP
import time

led_r =13
led_g = 19
sensor = 12

GP.setmode(GP.BCM)

GP.setup(led_r, GP.OUT)
GP.setup(led_g, GP.OUT)
GP.setup(sensor, GP.IN)

print("PIR Ready....")
time.sleep(5)

try:
    while True:
        if GP.input(sensor) == 1:
            GP.output(led_g, 1)
            GP.output(led_r, 0)
            print("Motion Detected!!!!!!")
            time.sleep(0.2)

        if GP.input(sensor) == 0:
            GP.output(led_r, 1)
            GP.output(led_g, 0)
            time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopped by User")
    GP.cleanup()
