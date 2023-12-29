import _thread

from fast_rainbow import FastRainbow
from slow_rainbow import SlowRainbow


if __name__ == "__main__":
    fr = FastRainbow(0, 27)
    sr = SlowRainbow(1, 28)
    
    while True:
        fr.draw()
        sr.draw()
