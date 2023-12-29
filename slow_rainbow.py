import random
import time
from neopixel import Neopixel

PIXELS = 300

START = 0
END = PIXELS - 1 

COL_WHITE = (255, 255, 255)
COL_BLACK = (0, 0, 0)
COL_RED = (255, 0, 0)
COL_BLUE = (0, 0, 255)
COL_ORANGE = (255, 50, 0)
COL_YELLOW = (255, 100, 0)
COL_GREEN = (0, 255, 0)
COL_INDIGO = (100, 0, 90)
COL_VIOLET = (200, 0, 100)

COLOURS_RGB = [COL_RED, COL_ORANGE, COL_YELLOW, COL_GREEN, COL_BLUE, COL_INDIGO, COL_VIOLET]


class SlowRainbow:
    strip = None


    def __init__(self, state_machine, gpio_port):
        self.strip = Neopixel(PIXELS, state_machine, gpio_port, "GRB")
        self.strip.brightness(100)
        s_step = round(PIXELS / len(COLOURS_RGB))
        s_current_pixel = START

        for color1, color2 in zip(COLOURS_RGB, COLOURS_RGB[1:]):
            self.strip.set_pixel_line_gradient(s_current_pixel, s_current_pixel + s_step, color1, color2)
            s_current_pixel += s_step


        self.strip.set_pixel_line_gradient(s_current_pixel, END, COL_VIOLET, COL_RED)
        self.strip.show()


    def draw(self):
        self.strip.rotate_right(1)
        self.strip.show()
