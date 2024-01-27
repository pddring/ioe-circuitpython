import colorsys
import time
import board
from ioexpander.devices import RGBLED

print("""rgbled.py

Demonstrates running a common-cathode RGB LED, or trio of LEDs wired between each PWM pin and Ground.

You must wire your Red, Green and Blue LEDs or LED elements to pins 1, 7 and 2

Press Ctrl+C to exit.

""")

LED_R = 1
LED_G = 7
LED_B = 2


if __name__ == "__main__":
    rgbled = RGBLED(None, 0x0F, LED_R, LED_G, LED_B, brightness=0.5, invert=True)

    while True:
        h = time.time() % 256 / 256
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        print(h, r, g, b)
        rgbled.set_rgb(r, g, b)
        time.sleep(1.0 / 30)
