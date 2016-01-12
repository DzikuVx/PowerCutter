PowerCutter
===========

Simple 3.3V power source for Raspberry Pi pheripherials. Power source can be switched on/off using one of Raspberry Pi GPIOs.

#Requirements:
* Raspberry Pi
* Python
* RPi.GPIO module https://pypi.python.org/pypi/RPi.GPIO

#Parts:
* 4.7 kOhm resistor
* 470 Ohm resistor
* 2x 100nF capacitors
* BC547 transistor
* BD139 transistor
* LM7833 Voltage regulator

![Schema](schema.png)
![Example](img.jpg)

#Notes

In this configuration BD139 transistor can provide up to 300mA without voltage drop. Although LM7833 can live with this, I suggest not to draw more than 250mA from device.