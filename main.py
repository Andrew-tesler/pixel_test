"""NeoPixel LED Demo."""
# from machine import Pin
# from adafruit_pixelbuf import PixelBuf
from neopixel import NeoPixel
from machine import Pin, ADC, RTC
from time import sleep
from random import *
from urandom import *
import random
# import numpy as np  

# Global defines for the LED strip
LED_COUNT       = 288      # Number of LED pixels.
NEOPIXEL_PIN    = 2       # GPIO pin connected to the pixels (must support PWM!).
BUTTON_PIN      = 6       # GPIO pin connected to button
PixelBuf        = 3       # Number for each pixel

MIN_COLOR      = 0       # Minimum color value
MAX_COLOR      = 5      # Maximum color value
# init function for the LED strip and button
NEOPIXEL_PIN   = Pin(NEOPIXEL_PIN, Pin.OUT)
BUTTON_PIN     = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Init Strip array - will use as global variable for the LED strip
STRIP_ARRAY = [[0 for x in range(3)] for y in range(LED_COUNT)]

# Init the LED strip
strip = NeoPixel(NEOPIXEL_PIN, LED_COUNT, timing=1)

# print(STRIP_ARRAY)
# run over the LED strip and set the color to black
for i in range(LED_COUNT):
    strip[i] = (0, 0, 0)
    strip.write()

# print strip attriputes
print("Strip length: ", strip.n)

print("Strip pin: ", strip.pin)
print("Strip pixel count: ", strip.n)

adc = ADC(Pin(26))     # create ADC object on ADC pin
adc.read_u16()         # read value, 0-65535 across voltage range 0.0v - 3.3v
print("Analog input pin: ", adc.read_u16() )

rtc = RTC()
rtc.datetime((2022, 7, 19, 2, 12, 30, 0, 0)) # set a specific date and
                                             # time, eg. 2017/8/23 1:12:48
print(rtc.datetime()) # get date and time

# # Testing the LED strip
# STRIP_ARRAY[2] = [125, 0, 10]

# strip[-1] = STRIP_ARRAY[2]
# np[pixel] = (i, i, i)
# Generate a random color with different values for each color
# R = randint(0, 20)
# G = randint(0, 20)
# B = randint(0, 20)

# main loop
while True:
    # check if the button is pressed
    if BUTTON_PIN.value() == 0:
        # set all leds to random color
        for i in range(LED_COUNT):
            STRIP_ARRAY[i][0] = randint(MIN_COLOR, MAX_COLOR)
            STRIP_ARRAY[i][1] = randint(MIN_COLOR, MAX_COLOR - STRIP_ARRAY[i][0])
            STRIP_ARRAY[i][2] = randint(MIN_COLOR, MAX_COLOR - STRIP_ARRAY[i][1])
            strip[i] = (STRIP_ARRAY[i])
            
            # sleep(0.01)
    # check if the button is not pressed
    else:
        # set all leds to Blue
        for i in range(LED_COUNT):
            strip[i] = (2, 0, 1)
           
            # sleep(0.01)
    # Update the LED strip with the new values from the array
    # for i in range(LED_COUNT):
        # strip[i] = STRIP_ARRAY[i]
    # print strip RGB values
    # print(strip.rgb)

    # print(strip.n)
    # get and print analog value of A1 pin
    # print(adc.read())
    # print("Analog input pin: ", adc.read_u16() )
    # strip.write()

    # strip.write()
# strip[2] = (200,0,0)

# def fade(np, pixel, brightness):
#     """Fade the given pixel in and out."""
#     for i in range(0, 255):
#         np[pixel] = (i, i, i)
#         np.write()
#         sleep(0.01)
#     for i in range(255, 0, -1):
#         np[pixel] = (i, i, i)
#         np.write()
#         sleep(0.01)

strip.write()

# # print button state
# def print_button_state():
#     print('Button state:', BUTTON_PIN.value())

# print_button_state()


# x = random.getrandbits(32)
# print("{}".format(x))

# # pin = Pin(4, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
# # np = NeoPixel(pin, LED_COUNT)   # create NeoPixel driver on GPIO0 for 4 pixels

# np[0] = (0, 0, 0)
# np[1] = (12, 0, 50)
# np[2] = (0, 12, 0)
# np[3] = (0, 0, 50)
# np.write()
# # sleep(3)
# pixel = [0, 1, 2]      # set first pixel to black


# def randrange(start, stop=None):
#     if stop is None:
#         stop = start
#         start = 0
#     upper = stop - start
#     bits = 0
#     pwr2 = 1
#     while upper > pwr2:
#         pwr2 <<= 1
#         bits += 1
#     while True:
#         r = getrandbits(bits)
#         if r < upper:
#             break
#     return r + start


# def randint(start, stop):
#     return randrange(start, stop + 1)

# # fade function from Adafruit NeoPixel library
# def fade(np, pixel, brightness):
#     """Fade the given pixel in and out."""
#     for i in range(0, 255):
#         np[pixel] = (i, i, i)
#         np.write()
#         sleep(0.01)
#     for i in range(255, 0, -1):
#         np[pixel] = (i, i, i)
#         np.write()
#         sleep(0.01)

# # blink all leds at random intervals and random colours
# while True:
#     for i in range(LED_COUNT):
#         np[i] = (randint(0, 125), randint(0, 125), randint(0, 125))
#         np.write()
        
#         # sleep(0.1)
#     sleep(randint(1, 3))   


# while True:
#     p = 0
#     for p in range(0, 3):
#         for n in range(10, 255):
#             pixel[p] = n
#             np[0] = pixel
#             np[1] = pixel
#             np[2] = pixel
#             np[3] = pixel
#             np.write()
#             sleep(0.1)
#         for n in range(10, 255):
#             pixel[p] = 255 - n
#             np[0] = pixel
#             np[1] = pixel
#             np[2] = pixel
#             np[3] = pixel
#             np.write()
#             sleep(0.1)


# # for p in pixel:
# #     print(p)
# #     for i in range(10, 255):
# #         np[0] = (i, 0, 0)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(10, 255):
# #         np[0] = (255-i, 0, 0)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(10, 255):
# #         np[0] = (0, i, 0)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(10, 255):
# #         np[0] = (0, 255-i, 0)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(10, 255):
# #         np[0] = (0, 0, i)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(10, 255):
# #         np[0] = (0, 0, 255-i)
# #         np.write()
# #         sleep(0.01)
   





        


# # np[0] = (125, 255, 0) # set the first pixel to white
# # np.write()              # write data to all pixels
# # r, g, b = np[0]         # get first pixel colour