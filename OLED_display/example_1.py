# this is an example built from the customer reviews for 128x64 OLED display on Amazon.
# product page: https://www.amazon.com/dp/B09C5K91H7
# Display driver chip is probably SSD1306 
#
# Here are the libraries you need from circuit python+adafruit to get this to work:
# 	adafruit_bitmap_font  
#	adafruit_display_text  
#	adafruit_displayio_layout  
#	adafruit_displayio_ssd1306.mpy
# downloaded from: https://circuitpython.org/libraries 
# explained at https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries

import board
import busio
import displayio
import i2cdisplaybus
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout

displayio.release_displays()

i2c = busio.I2C(scl=board.GP21, sda=board.GP20)
displayBus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(displayBus, width=128, height=64)

# running just the commands above will echo the serial
# console to the OLED display

displayGroup = displayio.Group(scale=1, x=0, y=0)
display.root_group = displayGroup

layout = GridLayout(
    x=0,
    y=0,
    width=display.width,
    height=display.height,
    grid_size=(1,4),
    cell_padding=0,
    divider_lines=False
)

displayGroup.append(layout)

L1 = label.Label(terminalio.FONT,text="abcdefghijklmnopqrstu")
L2 = label.Label(terminalio.FONT,text="qrstuvwxyz 123456789")
L3 = label.Label(terminalio.FONT,text="ABCDEFGHIJKLMNOP")
L4 = label.Label(terminalio.FONT,text="QRSTUVWXYZ")
#L5 = label.Label(terminalio.FONT,text="!@#$%^&*()_+", color=0xffffff)

layout.add_content(L1, grid_position=(0, 0), cell_size=(1,1) )
layout.add_content(L2, grid_position=(0, 1), cell_size=(1,1) )
layout.add_content(L3, grid_position=(0, 2), cell_size=(1,1) )
layout.add_content(L4, grid_position=(0, 3), cell_size=(1,1) )
#layout.add_content(L5, grid_position=(0, 4), cell_size=(1,1) )

while (True) :
    pass

'''
# Here's a trimmed down version that also works.
# pulling from 
# https://docs.circuitpython.org/projects/displayio_ssd1306/en/latest/examples.html
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = busio.I2C(scl=board.GP21, sda=board.GP20)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
splash = displayio.Group()

display.root_group = splash

text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=64 // 2 - 1)
splash.append(text_area)

while True:
    pass

'''
