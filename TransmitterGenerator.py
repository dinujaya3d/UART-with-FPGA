import RPi.GPIO as GPIO
import time

# Use Broadcom SOC Pin numbers
GPIO.setmode(GPIO.BCM)

# Setup the output GPIO pins
pins = [14, 15, 18, 23, 24, 25, 8, 7]  # Example GPIO pins
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def output_binary(number):
    binary_format = '{:08b}'.format(number)  # Format number as binary
    for i, bit in enumerate(binary_format):
        GPIO.output(pins[i], int(bit))  # Set each pin to high or low depending on bit value

try:
    while True:
        user_input = input("Enter a number (0-255): ")  # Get user input
        try:
            num = int(user_input)  # Convert input to integer
            if 0 <= num <= 255:
                output_binary(255-num)  # Output the number in binary on GPIO pins
                time.sleep(0.5)  # Wait half a second between updates
            else:
                print("Number out of range. Please enter a number between 0 and 255.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    GPIO.cleanup()  # Clean up GPIO on exit