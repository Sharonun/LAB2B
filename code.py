import time
import board
import digitalio
from adafruit_apds9960.apds9960 import APDS9960
i2c = board.STEMMA_I2C()
sensor = APDS9960(i2c)
sensor.enable_proximity = True

led = digitalio.DigitalInOut(board.SDA)
led.direction = digitalio.Direction.OUTPUT
gre = digitalio.DigitalInOut(board.SCL)
gre.direction = digitalio.Direction.OUTPUT

while True:
    gesture = sensor.proximity
    print(gesture)
    if gesture > 50:
        gre.value = False
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
    if gesture <50:
        gre.value = True


