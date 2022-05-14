import pibooth
import RPi.GPIO as GPIO

__version__ = "1.0.0"
RELAIS_1_GPIO = 17

@pibooth.hookimpl
def pibooth_startup(app):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

@pibooth.hookimpl
def state_preview_enter(app):
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

@pibooth.hookimpl
def state_capture_exit(app):
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)




