# Chaser effect. This uses our own framebuffer implementation.

import random
import time
from neopixel import Neopixel

PIXELS = 300
STEP = 1

START = 0
END = PIXELS - 1 

COL_WHITE = (255, 255, 255)
COL_BLACK = (0, 0, 0)
COL_RED = (255, 0, 0)
COL_BLUE = (0, 0, 255)


def get_colour(rgb, brightness = 255):
    return round(rgb[2] * (brightness / 255)) << 0 | round(rgb[0] * (brightness / 255)) << 8 | round(rgb[1] * (brightness / 255)) << 16


def update(strip, buffer):
    strip.pixels = buffer
    strip.show()
    
    
def wheel_color(position):
    if position < 0:
        position = 0
    if position > 384:
        position = 384

    if position < 128:
        r = 127 - position % 128
        g = position % 128
        b = 0
    elif position < 256:
        g = 127 - position % 128
        b = position % 128
        r = 0
    else:
        b = 127 - position % 128
        r = position % 128
        g = 0

    return (r, g, b)


class Chaser:
    strip = None
    
    buffer = [0] * PIXELS

    strip_forward = True
    color_pos = 0
    color_forward = True
        

    def __init__(self, state_machine, gpio_port):
        self.strip = Neopixel(PIXELS, state_machine, gpio_port, "GRB")
        self.strip.brightness(100)
        
        update(self.strip, self.buffer)


    def draw(self):
        if self.strip_forward:
            pixel_range = range(START + 1, END + 1, STEP)
        else:
            pixel_range = range(END - 1, START - 1, -STEP)
            
        for p in pixel_range:
            self.buffer = [0] * PIXELS
            self.buffer[p] = get_colour(wheel_color(self.color_pos))
            if self.color_pos == 384:
                self.color_forward = False
            
            if self.color_forward == True:
                self.color_pos = self.color_pos + 1
            else:
                self.color_pos = self.color_pos - 1
                
            if self.color_pos == -1:
                self.color_forward = True
                self.color_pos = 1
                                   
            update(self.strip, self.buffer)
        
        self.strip_forward = not self.strip_forward
