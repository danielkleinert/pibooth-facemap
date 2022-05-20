import pibooth
import RPi.GPIO as GPIO
from phue import Bridge

__version__ = "1.0.0"
RELAIS_1_GPIO = 17

hue = Bridge('192.168.178.174')


@pibooth.hookimpl
def pibooth_startup(app):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

@pibooth.hookimpl
def state_preview_enter(app):
    hue.set_light(3, {'transitiontime': 0, 'on': True, 'bri': 254})
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)

@pibooth.hookimpl
def state_capture_exit(app):
    hue.set_light(3, {'transitiontime': 0, 'on': False})
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)




