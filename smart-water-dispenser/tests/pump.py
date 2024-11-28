import RPi.GPIO as GPIO
import time

# Configure GPIO pins
trigger_pin = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(trigger_pin, GPIO.OUT)

def send_trigger_signal():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(trigger_pin, GPIO.LOW)

send_trigger_signal()