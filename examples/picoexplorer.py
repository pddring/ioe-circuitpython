import picoexplorer as display
import time
import random
import board
import ioexpander as io
import colorsys

count = 0

rgb = [0, 0, 0]
label_r = display.text("R: 0", 0, 10, 0, 2)
label_r.color = 0xFF0000

label_g = display.text("G: 0", 0, 30, 0, 2)
label_g.color = 0x00FF00

label_b = display.text("B: 0", 0, 50, 0, 2)
label_b.color = 0x0000FF

color_bar = display.rectangle(40, 100, 160, 100)

I2C_ADDR = 0x0F  

PIN_RED = 1
PIN_GREEN = 7
PIN_BLUE = 2

POT_ENC_A = 12
POT_ENC_B = 3
POT_ENC_C = 11

BRIGHTNESS = 1.0                # Effectively the maximum fraction of the period that the LED will be on
PERIOD = int(255 / BRIGHTNESS)  # Add a period large enough to get 0-255 steps at the desired brightness

ioe = io.IOE(i2c_addr=I2C_ADDR, interrupt_pin=board.GP22, SDA=board.GP20, SCL=board.GP21)

# Swap the interrupt pin for the Rotary Encoder breakout
if I2C_ADDR == 0x0F:
    ioe.enable_interrupt_out(pin_swap=True)

ioe.setup_rotary_encoder(1, POT_ENC_A, POT_ENC_B, pin_c=POT_ENC_C)

ioe.set_pwm_period(PERIOD)
ioe.set_pwm_control(divider=2)  # PWM as fast as we can to avoid LED flicker

ioe.set_mode(PIN_RED, io.PWM, invert=True)
ioe.set_mode(PIN_GREEN, io.PWM, invert=True)
ioe.set_mode(PIN_BLUE, io.PWM, invert=True)


while True:
    if ioe.get_interrupt():
        count = ioe.read_rotary_encoder(1)
        ioe.clear_interrupt()

    ioe.output(PIN_RED, rgb[0])
    ioe.output(PIN_GREEN, rgb[1])
    ioe.output(PIN_BLUE, rgb[2])
    
    rgb = colorsys.hsv_to_rgb((count % 255)/ 255, 1, 1)
    
    label_r.text = "R: {}".format(rgb[0])
    label_g.text = "G: {}".format(rgb[1])
    label_b.text = "B: {}".format(rgb[2])
    color_bar.fill = rgb[0] << 16 | rgb[1] << 8 | rgb[2]
    
    time.sleep(.1)