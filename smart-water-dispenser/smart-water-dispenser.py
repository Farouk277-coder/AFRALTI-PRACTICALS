import RPi.GPIO as GPIO
import time

# Configure GPIO pins
trigger_pin = 18
echo_pin = 24
relay_pin = 23

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set trigger pin as output and echo pin as input
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)  

GPIO.setup(relay_pin, GPIO.OUT)

def distance_measurement():
    # Set trigger pin low for 0.01 seconds
    GPIO.output(trigger_pin, False)
    time.sleep(0.01)

    # Set trigger pin high for 0.01 seconds
    GPIO.output(trigger_pin, True)
    time.sleep(0.01)
    GPIO.output(trigger_pin, False)

    # Measure pulse duration
    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end  
    pulse_start

    # Calculate distance
    distance = pulse_duration * 17150
    distance = round(distance, 2)

def control_water_flow (distance):
    if distance < 20:  # Adjust threshold as needed
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn on water flow
    else:
        GPIO.output(relay_pin, GPIO.LOW)  # Turn off water flo

try:
    while True:
        distance = distance_measurement()
        print("Distance:", distance, "cm")
        control_water_flow(distance)
        time.sleep(1)  # Adjust delay as needed

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

