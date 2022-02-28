"""NeoPixel LED Demo."""
# from machine import Pin
from neopixel import NeoPixel
from machine import Pin
from time import sleep
from random import *
from urandom import *


LED_COUNT = 4

print('Testing')

import random
x = random.getrandbits(32)
print("{}".format(x))

pin = Pin(4, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, LED_COUNT)   # create NeoPixel driver on GPIO0 for 4 pixels

np[0] = (0, 0, 0)
np[1] = (12, 0, 50)
np[2] = (0, 12, 0)
np[3] = (0, 0, 50)
np.write()
# sleep(3)
pixel = [0, 1, 2]      # set first pixel to black


def randrange(start, stop=None):
    if stop is None:
        stop = start
        start = 0
    upper = stop - start
    bits = 0
    pwr2 = 1
    while upper > pwr2:
        pwr2 <<= 1
        bits += 1
    while True:
        r = getrandbits(bits)
        if r < upper:
            break
    return r + start


def randint(start, stop):
    return randrange(start, stop + 1)

# fade function from Adafruit NeoPixel library
def fade(np, pixel, brightness):
    """Fade the given pixel in and out."""
    for i in range(0, 255):
        np[pixel] = (i, i, i)
        np.write()
        sleep(0.01)
    for i in range(255, 0, -1):
        np[pixel] = (i, i, i)
        np.write()
        sleep(0.01)

# blink all leds at random intervals and random colours
while True:
    for i in range(LED_COUNT):
        np[i] = (randint(0, 125), randint(0, 125), randint(0, 125))
        np.write()
        
        # sleep(0.1)
    sleep(randint(1, 3))   


while True:
    p = 0
    for p in range(0, 3):
        for n in range(10, 255):
            pixel[p] = n
            np[0] = pixel
            np[1] = pixel
            np[2] = pixel
            np[3] = pixel
            np.write()
            sleep(0.1)
        for n in range(10, 255):
            pixel[p] = 255 - n
            np[0] = pixel
            np[1] = pixel
            np[2] = pixel
            np[3] = pixel
            np.write()
            sleep(0.1)


# for p in pixel:
#     print(p)
#     for i in range(10, 255):
#         np[0] = (i, 0, 0)
#         np.write()
#         sleep(0.01)
#     for i in range(10, 255):
#         np[0] = (255-i, 0, 0)
#         np.write()
#         sleep(0.01)
#     for i in range(10, 255):
#         np[0] = (0, i, 0)
#         np.write()
#         sleep(0.01)
#     for i in range(10, 255):
#         np[0] = (0, 255-i, 0)
#         np.write()
#         sleep(0.01)
#     for i in range(10, 255):
#         np[0] = (0, 0, i)
#         np.write()
#         sleep(0.01)
#     for i in range(10, 255):
#         np[0] = (0, 0, 255-i)
#         np.write()
#         sleep(0.01)
   





        


# np[0] = (125, 255, 0) # set the first pixel to white
# np.write()              # write data to all pixels
# r, g, b = np[0]         # get first pixel colour