import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module
from gpiozero import DistanceSensor  # Import the DistanceSensor class from gpiozero

# To define GPIO pin numbers for LED, ultrasonic sensor trigger, and echo pins
LED_PIN = 16
TRIGGER_PIN = 20
ECHO_PIN = 21

# To set up GPIO
GPIO.setwarnings(False)  # To ignore warning messages
GPIO.setmode(GPIO.BCM)  # To use the Broadcom SOC channel numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # To set LED_PIN as an output pin

# To create a PWM object for the LED
# To create a PWM object for LED at 30 Hz
led_pwm = GPIO.PWM(LED_PIN, 30)  
# To start PWM with a duty cycle of 0 (LED off)
led_pwm.start(0)  

# To create an ultrasonic distance sensor object
distance_sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIGGER_PIN, max_distance=1.0)

try:
    while True:
        sleep(1)  # To wait for 1 second
        # To read the distance from the ultrasonic sensor and convert to centimeters
        distance_cm = distance_sensor.distance * 100
        # To print the distance with 2 decimal places
        print(f"Object Distance (CM): {distance_cm:.2f}")
        
        # T calculate LED brightness based on distance (inverse relation)
        brightness = 100 - round(distance_cm)
        # T ensure brightness stays within the range of 0 to 100
        brightness = max(0, min(100, brightness))
        # T set the LED brightness using PWM
        led_pwm.ChangeDutyCycle(brightness)

except KeyboardInterrupt:
    pass

# T clean up GPIO settings and stop PWM
led_pwm.stop()
GPIO.cleanup()