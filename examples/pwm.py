import colorsys
import time
import board
import ioexpander as io

print("""pwm.py

Demonstrates running a common-cathode RGB LED, or trio of LEDs wired between each PWM pin and Ground.

You must wire your Red, Green and Blue LEDs or LED elements to pins 1, 7 and 2.

Press Ctrl+C to exit.

""")

PIN_RED = 1
PIN_GREEN = 7
PIN_BLUE = 2

BRIGHTNESS = 0.05               # Effectively the maximum fraction of the period that the LED will be on
PERIOD = int(255 / BRIGHTNESS)  # Add a period large enough to get 0-255 steps at the desired brightness

ioe = io.IOE(i2c_addr=0x0F, SDA=board.GP20, SCL=board.GP21)

ioe.set_pwm_period(PERIOD)
ioe.set_pwm_control(divider=1)  # PWM as fast as we can to avoid LED flicker

ioe.set_mode(PIN_RED, io.PWM)
ioe.set_mode(PIN_GREEN, io.PWM)
ioe.set_mode(PIN_BLUE, io.PWM)

print("Running LED with {} brightness steps.".format(int(PERIOD * BRIGHTNESS)))

while True:
    h = round(time.time() % 256 / 256, 2)
    r, g, b = [int(c * PERIOD * BRIGHTNESS / 256) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
    print(h, r, g, b)
    ioe.output(PIN_RED, r)
    ioe.output(PIN_GREEN, g)
    ioe.output(PIN_BLUE, b)

    time.sleep(1.0 / 30)
