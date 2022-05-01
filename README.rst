PewPew LCD
**********

PewPew LCD is a handheld gaming device designed for use in programming
workshops. Because it runs CircuitPython, you don't have to install anything on
your computer to program it: you just edit a text file on the USB drive that
appears when you connect the device.

There is a whole family of compatible PewPew devices, and PewPew LCD is just
one of them. It's distinguished by the use of a low-power monochrome LCD
display for the screen — which makes it cheap, battery-efficient, and lets you
see the error messages from your code on the screen,  without having to use any
special programs to connect to the serial console.

Hardware
========

In this repository you will find the schematic, the bill of materials, the
design files and the generated gerber and pnp files, for building PewPew LCD.
You can either assemble it yourself, or use a fabrication service to do it
for you.


Software
========

For the device to function properly, it has to be loaded with proper software.
To do that, you will need a CMSIS/DAP-compatible programmer to flash the
bootloader on the microcontroller, and then you will need CircuitPython
firmware for this device, which can be flashed over USB once the bootloader is
in place. It's also convenient to put a menu program for selecting the game to
play on the device as main.py.

This device uses the same bootloader as fluff_m0. Both compiled binaries and
source code for that bootloader can be obtained from: https://github.com/adafruit/uf2-samdx1/releases/

In order to flash the bootloader, the programmer needs to be connected to the
expansion port at the bottom of the device, to pins marked as "-" for GND, "1"
for SWC, "2" for SWD, and + for 3.3V. Unless the programmer provides its own
power, the USB cable also needs to be connected, and the power switch switched
to the "USB" position. The bootloader binary needs to be flashed at address 0.

Once the bootloader is in place, a UF2 file with CircuitPython can be obtained
from the https://circuitpython.org website, or compiled from source code as per
CircuitPython's building instructions. Then the file can be copied to the
device over USB.

Once the firmware is in place, the menu program and any other programs desired
can be simply copied onto the device over USB.
