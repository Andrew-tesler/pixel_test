"""NeoPixel LED Demo."""
# from machine import Pin
# from adafruit_pixelbuf import PixelBuf
from neopixel import NeoPixel
from machine import Pin, ADC, RTC
from time import sleep
import time
from random import *
from urandom import *
import random
x = random.getrandbits(24)

MAX_BRIGHTNESS = 70
MIN_BRIGHTNESS = 1
GLOBAL_BRIGHTNESS = 25

GLOBAL_COLOR = (0, 0, 0)
GLOBAL_COLOR_CHANGE_SPEED = 0.1

# TODO - strucure the code for additinal lamps and add a function to set the color of all lamps

# There is several Mushrooms each with diferent size ( LED QTY )
# Global Button to turn on/off all Mushrooms
# Global Brightness control
# Global Color control
# Global Color change speed control

# dictioanry to hold the lamp data leds, pin, brightness, color, speed
# lamps = { 'lamp1': {'leds': 24, 'pin': 2, 'brightness': 0.5, 'color': (255, 0, 0), 'speed': 0.5}, 'lamp2': {'leds': 12, 'pin': 4, 'brightness': 0.5, 'color': (0, 255, 0), 'speed': 0.5}, 'lamp3': {'leds': 6, 'pin': 5, 'brightness': 0.5, 'color': (0, 0, 255), 'speed': 0.5} }
MUSHROOMS = {'mush1': {'leds': 24, 'pin': 2, 'brightness': 20, 'color': (0, 1, 1), 'speed': 1000000, 'time': 0, 'dir': 1, 'max_color': (0,70,70)},
             'mush2': {'leds': 24, 'pin': 3, 'brightness': 20, 'color': (1, 1, 0), 'speed': 1000000, 'time': 0, 'dir': 0, 'max_color': (30,25,0)},
             'mush3': {'leds': 16, 'pin': 4, 'brightness': 20, 'color': (0, 0, 1), 'speed': 10000, 'time': 0, 'dir': 0, 'max_color': (0,0,50)},
             'mush4': {'leds': 8, 'pin': 6, 'brightness': 20, 'color': (1, 0, 1), 'speed': 10000, 'time': 0, 'dir': 1, 'max_color': (50,0,50)},
             'mush5': {'leds': 8, 'pin': 7, 'brightness': 20, 'color': (0, 0, 1), 'speed': 1000, 'time': 0, 'dir': 0, 'max_color': (0,0,100)},
             'mush6': {'leds': 8, 'pin': 8, 'brightness': 20, 'color': (0, 1, 0), 'speed': 10000, 'time': 0, 'dir': 1, 'max_color': (0,100,0)}}


# TODO - add a function to set the color of all lamps
# TODO - add a function to set the brightness of all lamps
# TODO - add a function to set the speed of all lamps
# TODO - add a function to set initial color of each lamp or change the fade function


# set the color of a lamp
def set_color(lamp, color):
    if lamp in MUSHROOMS:
        if MAX_BRIGHTNESS >= color[0] >= MIN_BRIGHTNESS and MAX_BRIGHTNESS >= color[1] >= MIN_BRIGHTNESS and MAX_BRIGHTNESS >= color[2] >= MIN_BRIGHTNESS:

            MUSHROOMS[lamp]['color'] = color
            # print('color set to: ', color)


### Time functions ###
# get time right now
def get_time():
    return time.time()


# set lamp time
def set_time(lamp, time):
    if lamp in MUSHROOMS:
        MUSHROOMS[lamp]['time'] = time


# Get Lamp time
def get_lmp_time(lamp):
    if lamp in MUSHROOMS:
        return MUSHROOMS[lamp]['time']


# Store the time for the lamp
def store_time(lamp):
    if lamp in MUSHROOMS:
        # time.ticks_us()
        MUSHROOMS[lamp]['time'] = time.ticks_us()


# check if the time of a lamp is over
def check_time(lamp):
    if lamp in MUSHROOMS:
        if time.ticks_diff(time.ticks_us(), MUSHROOMS[lamp]['time']) >  MUSHROOMS[lamp]['speed']:
            # print('time diff: ', time.ticks_diff(time.ticks_us(), MUSHROOMS[lamp]['time']))
        # if get_time() - get_lmp_time(lamp) > MUSHROOMS[lamp]['speed']:  # type: ignore
            store_time(lamp)
            return True
        else:
            return False


# print check time result of all lamps
def print_check_time():
    for lamp in MUSHROOMS:
        print(lamp, check_time(lamp))


# set the brightness of a lamp
def set_brightness(lamp, brightness):
    if lamp in MUSHROOMS:
        if MAX_BRIGHTNESS >= brightness >= MIN_BRIGHTNESS:
            MUSHROOMS[lamp]['brightness'] = brightness




### Color functions ###

# Generate random color
def random_color():
    return (randrange(MIN_BRIGHTNESS, MAX_BRIGHTNESS), randrange(MIN_BRIGHTNESS, MAX_BRIGHTNESS), randrange(MIN_BRIGHTNESS, MAX_BRIGHTNESS))


# Fade the color of a lamp, until the max or min brightness is reached
# param: lamp - the lamp to fade
# param: direction - to fade 1 brightness up, 0 brightness down
def fade_color(lamp, direction):
    if lamp in MUSHROOMS:
        countUp = 0
        countDown = 0
        # print("..'fade_color'..")
        if direction == 1:
            if MUSHROOMS[lamp]['color'][0] == 0:
                pass
            else:
                if MUSHROOMS[lamp]['color'][0] < MUSHROOMS[lamp]['max_color'][0]:
                    MUSHROOMS[lamp]['color'] = (MUSHROOMS[lamp]['color'][0] + 1, MUSHROOMS[lamp]['color'][1], MUSHROOMS[lamp]['color'][2])
                    # print('color up: ', MUSHROOMS[lamp]['color'])
                    countUp += 1
            if MUSHROOMS[lamp]['color'][1] == 0:
                pass
            else:
                if MUSHROOMS[lamp]['color'][1] < MUSHROOMS[lamp]['max_color'][1]:
                    MUSHROOMS[lamp]['color'] = (MUSHROOMS[lamp]['color'][0], MUSHROOMS[lamp]['color'][1] + 1, MUSHROOMS[lamp]['color'][2])
                    countUp += 1
            if MUSHROOMS[lamp]['color'][2] == 0:
                pass
            else:
                if MUSHROOMS[lamp]['color'][2] < MUSHROOMS[lamp]['max_color'][2]:
                    MUSHROOMS[lamp]['color'] = (MUSHROOMS[lamp]['color'][0], MUSHROOMS[lamp]['color'][1], MUSHROOMS[lamp]['color'][2] + 1)
                    countUp += 1
            if countUp == 0:
                MUSHROOMS[lamp]['dir'] = 0

        if direction == 0:
            if MUSHROOMS[lamp]['color'][0] == 0:
                pass
            else:
                if MUSHROOMS[lamp]['color'][0] > MIN_BRIGHTNESS:
                    MUSHROOMS[lamp]['color'] = (MUSHROOMS[lamp]['color'][0] - 1, MUSHROOMS[lamp]['color'][1], MUSHROOMS[lamp]['color'][2])
                    countDown += 1
            if MUSHROOMS[lamp]['color'][1] == 0:
                pass
            else:
                if MUSHROOMS[lamp]['color'][1] > MIN_BRIGHTNESS:
                    MUSHROOMS[lamp]['color'] = (MUSHROOMS[lamp]['color'][0], MUSHROOMS[lamp]['color'][1] - 1, MUSHROOMS[lamp]['color'][2])  
                    countDown += 1
            if MUSHROOMS[lamp]['color'][2] == 0:
                pass
            else:
                if MUSHROOMS[lamp]['color'][2] > MIN_BRIGHTNESS:
                    MUSHROOMS[lamp]['color'] = (MUSHROOMS[lamp]['color'][0], MUSHROOMS[lamp]['color'][1], MUSHROOMS[lamp]['color'][2] - 1)
                    countDown += 1
            if countDown == 0:
                MUSHROOMS[lamp]['dir'] = 1
    else:   
        print('lamp not found')
    
            # print('color before: ', color)
            
            # print('color after: ', color)
           

# set_color('mush1', random_color())
# set_color('mush2', random_color())
# set_color('mush3', random_color())
# set_color('mush4', random_color())
# set_color('mush5', random_color())


# Print Welcome message for debugging purposes
print("Welcome to NeoPixel LED Demo")

# print all the lamps
print(MUSHROOMS)

# init the lamps
for lamp in MUSHROOMS:
    MUSHROOMS[lamp]['np'] = NeoPixel(
        Pin(MUSHROOMS[lamp]['pin']), MUSHROOMS[lamp]['leds'])

# turn on all lamps
for lamp in MUSHROOMS:
    MUSHROOMS[lamp]['np'].fill(MUSHROOMS[lamp]['color'])
    MUSHROOMS[lamp]['np'].write()

print("{}".format(x))

# loop through the lamps and set the color of each lamp each time the loop runs
while True:
    # print('#######################loop#############################')
    # print color of first lamp
    # print(MUSHROOMS['mush1']['color'])

    sleep(0.1) # sleep for 0.1 seconds for debugging purposes
    for lamp in MUSHROOMS:
        MUSHROOMS[lamp]['np'].fill(MUSHROOMS[lamp]['color'])
        MUSHROOMS[lamp]['np'].write()
        # check all mushrooms if the time is over
        if check_time(lamp):
            if MUSHROOMS[lamp]['dir'] == 1:
                fade_color(lamp, 1)
            else:
                fade_color(lamp, 0)
        else:
            pass

    
            # fill the lamp with the new color



            # fade the lamp color
            # fade_color(lamp, 1)
            # # set the lamp color
            # set_color(lamp, MUSHROOMS[lamp]['color'])
            # print the lamp color
            # print(lamp, MUSHROOMS[lamp]['color'])
            # print the lamp brightness

        # fade_color(lamp)
            # set the color of the lamp
       
        
        # MUSHROOMS[lamp]['np'].fill(MUSHROOMS[lamp]['color'])
        
        # change the color of the lamp only if time has passed
        # if time has passed change the color of the lamp
        # if time has not passed do nothing
    # MUSHROOMS[lamp]['np'].write()
    # sleep(0.01)

# # # Global defines for the LED strip
# LED_COUNT       = 24      # Number of LED pixels.
# NEOPIXEL_PIN    = 2       # GPIO pin connected to the pixels (must support PWM!).
# BUTTON_PIN      = 6       # GPIO pin connected to button
# PixelBuf        = 3       # Number for each pixel


# init the NeoPixel object
# np = NeoPixel(Pin(NEOPIXEL_PIN), LED_COUNT)


# init all led strips to off
# for i in range(LED_COUNT):

# # turn all LEDs on green color
# np.fill((0, 125, 25))
# np.write()

# np[0] = (0, 0, 0)
# # np[1] = (12, 0, 50)
# # np[2] = (0, 12, 0)
# # np[3] = (0, 0, 50)
# # np.write()
# # # sleep(3)
# # pixel = [0, 1, 2]      # set first pixel to black

# MAX_BRIGHTNESS = 50
# TRANSITION_TIME = 0.01


# def set_color(np, pixel, color):
#     np[pixel] = color
#     np.write()

# def set_strip_color(np, color):
#     for i in range(0, LED_COUNT):
#         np[i] = color
#     np.write()

# # Init the LED strip
# strip = NeoPixel(NEOPIXEL_PIN, LED_COUNT)


# # create fade in/out effect for color change
# def fade_in_out(np, pixel, color, steps, delay):
#     for i in range(0, steps):
#         np[pixel] = (int(color[0] * i / steps), int(color[1] * i / steps), int(color[2] * i / steps))
#         np.write()
#         sleep(delay)
#     for i in range(steps, 0, -1):
#         np[pixel] = (int(color[0] * i / steps), int(color[1] * i / steps), int(color[2] * i / steps))
#         np.write()
#         sleep(delay)


# def fade_in(np, pixel, color, steps, delay):
#     for i in range(0, steps):
#         np[pixel] = (int(color[0] * i / steps), int(color[1] * i / steps), int(color[2] * i / steps))
#         np.write()
#         sleep(delay)

# def fade_out(np, pixel, color, steps, delay):
#     for i in range(steps, 0, -1):
#         np[pixel] = (int(color[0] * i / steps), int(color[1] * i / steps), int(color[2] * i / steps))
#         np.write()
#         sleep(delay)

# # strip[-1] = STRIP_ARRAY[2]
# # np[pixel] = (i, i, i)
# # Generate a random color with different values for each color
# # R = randint(0, 20)
# # G = randint(0, 20)
# # B = randint(0, 20)

# set_strip_color(np, (0, 0, 10))
# sleep(1)
# set_strip_color(np, (0, 10, 0))
# sleep(1)
# set_strip_color(np, (10, 0, 0))
# sleep(1)

# while True:
#     for i in range(0, 24):
#         fade_in(np, i, (0, 0, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_out(np, i, (0, 0, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_in(np, i, (0, MAX_BRIGHTNESS, 0), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_out(np, i, (0, MAX_BRIGHTNESS, 0), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_in(np, i, (MAX_BRIGHTNESS, 0, 0), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_out(np, i, (MAX_BRIGHTNESS, 0, 0), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_in(np, i, (MAX_BRIGHTNESS, 0, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_out(np, i, (MAX_BRIGHTNESS, 0, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_in(np, i, (MAX_BRIGHTNESS, MAX_BRIGHTNESS, 0), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_out(np, i, (MAX_BRIGHTNESS, MAX_BRIGHTNESS, 0), 10, TRANSITION_TIME)
#         sleep(0.1)

#     for i in range(0, 24):
#         fade_in(np, i, (0, MAX_BRIGHTNESS, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)
#     for i in range(0, 24):
#         fade_out(np, i, (0, MAX_BRIGHTNESS, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)
#     for i in range(0, 24):
#         fade_in(np, i, (MAX_BRIGHTNESS, MAX_BRIGHTNESS, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)
#     for i in range(0, 24):
#         fade_out(np, i, (MAX_BRIGHTNESS, MAX_BRIGHTNESS, MAX_BRIGHTNESS), 10, TRANSITION_TIME)
#         sleep(0.1)


# # def randrange(start, stop=None):
# #     if stop is None:
# #         stop = start
# #         start = 0
# #     upper = stop - start
# #     bits = 0
# #     pwr2 = 1
# #     while upper > pwr2:
# #         pwr2 <<= 1
# #         bits += 1
# #     while True:
# #         r = getrandbits(bits)
# #         if r < upper:
# #             break
# #     return r + start


# # def randint(start, stop):
# #     return randrange(start, stop + 1)

# # # fade function from Adafruit NeoPixel library
# # def fade(np, pixel, brightness):
# #     """Fade the given pixel in and out."""
# #     for i in range(0, 255):
# #         np[pixel] = (i, i, i)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(255, 0, -1):
# #         np[pixel] = (i, i, i)
# #         np.write()
# #         sleep(0.01)

# # pixel_r = (randint(0, 25), randint(0, 125), randint(0, 125))
# # # blink all leds at random intervals and random colours
# # while True:
#     # set_color(np, pixel[0], pixel_r)

# #     # pixel_r = (randint(0, 250), randint(0, 250), randint(0, 250))
# #     # for i in range(LED_COUNT):
# #     #     np[i] = pixel_r
# #     #     np.write()

# #     sleep(0.1)
# #     # sleep(randint(1, 3))


# # while True:
# #     p = 0
# #     for p in range(0, 3):
# #         for n in range(10, 255):
# #             pixel[p] = n
# #             np[0] = pixel
# #             np[1] = pixel
# #             np[2] = pixel
# #             np[3] = pixel
# #             np.write()
# #             sleep(0.1)
# #         for n in range(10, 255):
# #             pixel[p] = 255 - n
# #             np[0] = pixel
# #             np[1] = pixel
# #             np[2] = pixel
# #             np[3] = pixel
# #             np.write()
# #             sleep(0.1)


# # # for p in pixel:
# #     print(p)
# #     for i in range(10, 255):
# #         np[0] = (i, 0, 0)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(255, 0, -1):
# #         np[pixel] = (i, i, i)
# #         np.write()
# #         sleep(0.01)

# strip.write()

# # # print button state
# # def print_button_state():
# #     print('Button state:', BUTTON_PIN.value())

# # print_button_state()


# # x = random.getrandbits(32)
# # print("{}".format(x))

# # # pin = Pin(4, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
# # # np = NeoPixel(pin, LED_COUNT)   # create NeoPixel driver on GPIO0 for 4 pixels

# # np[0] = (0, 0, 0)
# # np[1] = (12, 0, 50)
# # np[2] = (0, 12, 0)
# # np[3] = (0, 0, 50)
# # np.write()
# # # sleep(3)
# # pixel = [0, 1, 2]      # set first pixel to black


# # def randrange(start, stop=None):
# #     if stop is None:
# #         stop = start
# #         start = 0
# #     upper = stop - start
# #     bits = 0
# #     pwr2 = 1
# #     while upper > pwr2:
# #         pwr2 <<= 1
# #         bits += 1
# #     while True:
# #         r = getrandbits(bits)
# #         if r < upper:
# #             break
# #     return r + start


# # def randint(start, stop):
# #     return randrange(start, stop + 1)

# # # fade function from Adafruit NeoPixel library
# # def fade(np, pixel, brightness):
# #     """Fade the given pixel in and out."""
# #     for i in range(0, 255):
# #         np[pixel] = (i, i, i)
# #         np.write()
# #         sleep(0.01)
# #     for i in range(255, 0, -1):
# #         np[pixel] = (i, i, i)
# #         np.write()
# #         sleep(0.01)

# # # blink all leds at random intervals and random colours
# # while True:
# #     for i in range(LED_COUNT):
# #         np[i] = (randint(0, 125), randint(0, 125), randint(0, 125))
# #         np.write()

# #         # sleep(0.1)
# #     sleep(randint(1, 3))


# # while True:
# #     p = 0
# #     for p in range(0, 3):
# #         for n in range(10, 255):
# #             pixel[p] = n
# #             np[0] = pixel
# #             np[1] = pixel
# #             np[2] = pixel
# #             np[3] = pixel
# #             np.write()
# #             sleep(0.1)
# #         for n in range(10, 255):
# #             pixel[p] = 255 - n
# #             np[0] = pixel
# #             np[1] = pixel
# #             np[2] = pixel
# #             np[3] = pixel
# #             np.write()
# #             sleep(0.1)


# # # for p in pixel:
# # #     print(p)
# # #     for i in range(10, 255):
# # #         np[0] = (i, 0, 0)
# # #         np.write()
# # #         sleep(0.01)
# # #     for i in range(10, 255):
# # #         np[0] = (255-i, 0, 0)
# # #         np.write()
# # #         sleep(0.01)
# # #     for i in range(10, 255):
# # #         np[0] = (0, i, 0)
# # #         np.write()
# # #         sleep(0.01)
# # #     for i in range(10, 255):
# # #         np[0] = (0, 255-i, 0)
# # #         np.write()
# # #         sleep(0.01)
# # #     for i in range(10, 255):
# # #         np[0] = (0, 0, i)
# # #         np.write()
# # #         sleep(0.01)
# # #     for i in range(10, 255):
# # #         np[0] = (0, 0, 255-i)
# # #         np.write()
# # #         sleep(0.01)


# # # np[0] = (125, 255, 0) # set the first pixel to white
# # # np.write()              # write data to all pixels
# # # r, g, b = np[0]         # get first pixel colour
