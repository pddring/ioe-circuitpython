# Multiple i2c devices
# By default all RGB encoder devices have i2c address 0x0F
import busio
import board
from ioexpander.devices import RGBLED
from ioexpander import IOE
import random
import time
LED_R = 1
LED_G = 7
LED_B = 2
POT_ENC_A = 12
POT_ENC_B = 3
POT_ENC_C = 11

i2c = busio.I2C(scl=board.GP21, sda=board.GP20)

while True:
    while i2c.try_lock() == False:
        pass
    devices = i2c.scan()
    i2c.unlock()

    print("Found {} devices".format(len(devices)))
    for i in range(len(devices)):
        print("[{}] Device address 0x{:02X}".format(i, devices[i]))
    try:
        i = int(input("Which one would you like to control? (or leave blank to attempt to connect to them all)"))
    except:
        i = -1
    if i >= 0 and i < len(devices):
        print("Working with device at address {:02X}".format(devices[i]))
        ioe = IOE(i2c_addr=devices[i], I2C=i2c)
        encoder = RGBLED(ioe, devices[i], LED_R, LED_G, LED_B, brightness=0.5, invert=True)
        rgb = [random.randint(0, 255) for c in range(3)]
        print("Setting colour to R:{} G:{} B:{}".format(*rgb))
        encoder.set_rgb(*rgb)
        
        if "y" in input("Would you like to change the i2c address (y/n)?").lower():
            
            new_address = int(input("Please enter new 2 digit hex i2c address (e.g. 0F):"), 16)
            if new_address >= 0 and new_address <= 0xFF:
                print("Setting old device at old i2c address 0x{:02X} to 0x{:02X}".format(devices[i], new_address))
            else:
                print("Invalid i2c address - no changes made")
            
            encoder.ioe.set_i2c_addr(new_address)
        
    else:
        print("Attempting to connect to all i2c devices")
        
        # fade in
        for address in devices:
            print("Connecting to device at i2c address 0x{:02X}".format(address))
            ioe = IOE(i2c_addr=address, I2C=i2c)
            ioe.setup_rotary_encoder(1, POT_ENC_A, POT_ENC_B, pin_c=POT_ENC_C)
            encoder = RGBLED(ioe, address, LED_R, LED_G, LED_B, brightness=0.5, invert=True)
            rgb = [random.randint(0, 255) for c in range(3)]
            print("Turn the encoder to fade from black to R:{} G:{} B:{}".format(*rgb))
            encoder.set_rgb(0,0,0)
            print("Twizzle the rotary encoder up to 10:")
            count = 0
            while count != 10:
                if ioe.get_interrupt():
                    count = abs(ioe.read_rotary_encoder(1))
                    ioe.clear_interrupt()
                    print(count)
                    faded_rgb = [int(c*count/10) for c in rgb]
                    encoder.set_rgb(*faded_rgb)
                time.sleep(0.01)
            
        # go through all hue
        for address in devices:
            print("Connecting to device at i2c address 0x{:02X}".format(address))
            ioe = IOE(i2c_addr=address, I2C=i2c)
            ioe.setup_rotary_encoder(1, POT_ENC_A, POT_ENC_B, pin_c=POT_ENC_C)
            encoder = RGBLED(ioe, address, LED_R, LED_G, LED_B, brightness=0.5, invert=True)
            print("Turn the encoder to change the hue")
            encoder.set_rgb(0,0,0)
            print("Twizzle the rotary encoder up to 64:")
            count = 0
            while count != 64:
                if ioe.get_interrupt():
                    count = abs(ioe.read_rotary_encoder(1))
                    ioe.clear_interrupt()
                    hue = count / 64
                    print("Encoder value: {}/64 Hue: {}/1.0".format(count, hue))
                    
                    encoder.set_hue(hue, 1.0, 1.0)
                time.sleep(0.01)
            