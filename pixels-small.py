from machine import Pin
from neopixel import NeoPixel
import time


print("pixels-small.py")
pin = Pin(2, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 64)   # create NeoPixel driver on GPIO0 for 8 pixels

colors = [(50, 0, 0), (0, 50, 0), (0, 0, 125)] # define a list of colors to loop through

# for i in range(40):
#     np[i] = (0, 0, 0)
#     


while True:
    for color in colors:
        for i in range(256):
            r = int(color[0] * i / 255)
            g = int(color[1] * i / 255)
            b = int(color[2] * i / 255)
            for j in range(len(np)):
                np[j] = (r, g, b, 0)
                np.write()
                time.sleep(0.01) # add a delay of 0.01 second between each color transition step

        for i in range(255, -1, -1):
            r = int(color[0] * i / 255)
            g = int(color[1] * i / 255)
            b = int(color[2] * i / 255)
            for j in range(len(np)):
                np[j] = (r, g, b, 0)
                np.write()
                time.sleep(0.01) # add a delay of 0.01 second between each color transition step
    
# np[0] = (255, 0, 0,0) # set the first pixel to white
# # np[1] = (0, 0, 0,0) # set the first pixel to white
# # np[2] = (0, 0, 0,0) # set the first pixel to white
# # np[3] = (0, 0, 0,0) # set the first pixel to white
# np.write()              # write data to all pixels
