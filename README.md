# IO Expander

This is a port of Pimoroni's io expander python library, adapted to be suitable for a raspberry pi pico running CircuitPython 8
Source: https://github.com/pimoroni/ioe-python

IO Expander Breakout uses a Nuvoton MS51 microcontroller and I2C to give you 14 additional input/output pins to connect things up to. Eight of the pins are hooked up to an Analog to Digital Converter and six of the pins can be used as (up to 16-bit) PWM outputs.

This library is also used to power Pimoroni's other Nuvoton-based boards and breakouts.

It's only been tested with a RGB Encoder Breakout (see below) with a Raspberry Pi Pico on a Pico Explorer board so may need some adapting for other breakouts

## Where to buy

### HATs

* Weather HAT: https://shop.pimoroni.com/products/weather-hat-only
* Inventor HAT Mini: https://shop.pimoroni.com/products/inventor-hat-mini


### Breakouts

* IO Expander Breakout: https://shop.pimoroni.com/products/io-expander <== untested
* RGB Potentiometer Breakout: https://shop.pimoroni.com/products/rgb-potentiometer-breakout <== untested
* RGB Encoder Breakout: https://shop.pimoroni.com/products/rgb-encoder-breakout  <==  this is the only one I've tested it with ( I don't have any of the other breakouts)
* MICS6814 3-in-1 Gas Sensor Breakout: https://shop.pimoroni.com/products/mics6814-gas-sensor-breakout <== untested


# Getting the Library

Copy the ioexpander folder to your CircuitPython device's lib folder.
You may also need to copy the circuitpython_adapter folder into the lib folder (source: https://github.com/pimoroni/circuitpython_adapter)


# Examples and Usage

There are various examples to get you started with your IO Expander. With the library installed on your Raspberry Pi Pico, these can be found in the `~/examples` directory.

To take IO Expander further, the full API is described in the [library reference](/REFERENCE.md), with additional feature specific information found in the [docs folder](/docs).

# Multiple breakouts

It's possible to connect multiple devices to the same i2c bus as long as they have different addresses. 

You can change the default i2c address by connecting just that one breakout and calling the `set_i2c_addr method`. 
The [multiple_encoders](/examples/multiple_encoders.py) example allows you to change i2c addresses and experiment with multiple rgb rotary encoders