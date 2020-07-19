#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 by Murray Altheim. All rights reserved. This file is part
# of the pimain2ardsubordinate project and is released under the MIT Licence;
# please see the LICENSE file included as part of this package.
#
# author:   Murray Altheim
# created:  2020-04-30
# modified: 2020-05-04
#
# This test blinks an LED connected to pin 5 of the Arduino. This requires 
# a Raspberry Pi connected to an Arduino over I²C on address 0x08. Because
# an LED cannot directly handle a 5 volt supply you should connect the LED
# to ground through a resistor of about 330 ohms. The exact value will
# depend on the dropping voltage of the LED (which varies) and how bright
# you want it to appear.
#
# This also requires installation of pigpio, e.g.:
#
#   % sudo pip3 install pigpio
#

from lib.logger import Level
from lib.i2c_main import I2cMain

# ..............................................................................
def main():

    try:

        _device_id = 0x08  # must match Arduino's SLAVE_I2C_ADDRESS
        _main = I2cMain(_device_id, Level.INFO)
        if _main is not None: 

            _main.test_blink_led(7) # see documentation for hardware configuration

        else:
            raise Exception('unable to establish contact with Arduino on address 0x{:02X}'.format(_device_id))

    except KeyboardInterrupt:
        self._log.warning('Ctrl-C caught; exiting...')
    finally:
        if _main:
            _main.close()


if __name__== "__main__":
    main()

#EOF
