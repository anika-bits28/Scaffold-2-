# Import the necessary libraries
# - TouchPad: For using the capacitive touch sensor
# - Pin: To define the GPIO pins used
# - PWM: For controlling servo motors
# - neopixel: To control NeoPixel LEDs (WS2812)
# - time: To add delays and time-based operations

from machine import TouchPad, Pin, PWM
import machine
import neopixel
import time

# --- Touch Sensor Setup ---
# The touch sensor is connected to Pin 32.
# This sensor detects human touch and acts as an ON/OFF switch.
touch = TouchPad(Pin(32))

# The threshold defines how sensitive the touch sensor is.
# Adjust this value based on your specific hardware setup.
threshold = 200

# --- Neopixel LED Setup ---
# NeoPixel LEDs allow for full RGB control.
# Define the number of LEDs in your strip or ring.
NUM_LEDS = 16

# Define which GPIO pin the NeoPixel data line is connected to.
npLED = 5

# Initialize the NeoPixel object
np = neopixel.NeoPixel(machine.Pin(npLED), NUM_LEDS)

# Define an array of colors to create an "ocean effect"
# Colors are in (Red, Green, Blue) format
OCEAN_COLORS = [
    (0, 0, 30), (0, 0, 50), (0, 20, 100), (0, 50, 150),
    (0, 80, 180), (0, 100, 200), (0, 130, 220), (0, 160, 240),
    (0, 180, 255), (0, 200, 255), (10, 150, 80), (20, 180, 100),
    (0, 40, 120), (0, 60, 170), (0, 90, 210)  # Added deeper blue shades
]

# --- Servo Motor Setup ---
# PWM (Pulse Width Modulation) is used to control servos.
# The frequency of 50 Hz is the standard for servo motors.

servo1 = PWM(Pin(22), freq=50)  # Servo 1 on Pin 22
servo2 = PWM(Pin(26), freq=50)  # Servo 2 on Pin 26

# Set servos to their neutral position (90-degree angle)
servo1.duty(90)
servo2.duty(90)

# --- Main Loop ---
# The program continuously checks if the touch sensor is activated.
# If touched, it activates the servos and LED sequence.
while True:
    capacitiveValue = touch.read()  # Read the touch sensor value

    if capacitiveValue < threshold:  # If touched, turn everything ON
        print(" Emergency Alert! - System Activated ")

        # Move Servo 2 to the first position
        servo2.duty(50)

        # Start LED animation sequence
        start_time = time.ticks_ms()  # Get the current time
        for color in OCEAN_COLORS:
            for i in range(NUM_LEDS):  # Apply the color to all LEDs
                np[i] = color
            np.write()  # Send data to LEDs
            time.sleep(0.1)  # Short delay for smooth transition

            # Move Servo 1 back and forth for the first part of animation
            if time.ticks_diff(time.ticks_ms(), start_time) < 1000:
                servo1.duty(70)  # Move servo
                time.sleep(0.25)
                servo1.duty(90)  # Return to neutral
                time.sleep(0.25)

        # Move Servo 2 to the opposite position
        servo2.duty(110)

        # Start reverse LED animation sequence
        start_time = time.ticks_ms()
        for color in reversed(OCEAN_COLORS):  # Reverse the LED color order
            for i in range(NUM_LEDS):
                np[i] = color
            np.write()
            time.sleep(0.1)

            # Continue moving Servo 1 during the second animation phase
            if time.ticks_diff(time.ticks_ms(), start_time) < 1000:
                servo1.duty(70)
                time.sleep(0.25)
                servo1.duty(90)
                time.sleep(0.25)

    else:  # If NOT touched, turn everything OFF
        print(" Whoops - System is OFF ")

        # Turn off all NeoPixel LEDs (set them to black)
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        np.write()

        # Stop servo movement (return to neutral position)
        servo1.duty(90)
        servo2.duty(90)

    time.sleep(0.1)  # Small delay to prevent excessive looping
