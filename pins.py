# pins class that collects all the pins and their functions
# implimented for:
#   - WEMOS D1 Rev 3.0
# Author: Andrew Tesler
# Date: 2022-02-27


class wemos_pins:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Home with {} rooms and {} stories".format(self.name)



# ESP8266 pins and board name mapping
PINS = {'D0': 16, 'D1': 5, 'D2': 4, 'D3': 0, 'D4': 2, 'D5': 14, 'D6': 12, 'D7': 13, 'D8': 15}

PINS_GLOBAL = {
    'D0' :
            {'gpio' : 16, 'state': 0},
    'D1' :
            {'gpio' : 5, 'state' : 0},
    'D2' :
            {'gpio' : 4, 'state' : 0},
    'D3' :
            {'gpio' : 0, 'state' : 0},
    'D4' :
            {'gpio' : 2, 'state' : 0},
    'D5' :
            {'gpio' : 14, 'state' : 0},
    'D6' :
            {'gpio' : 12, 'state' : 0},
    'D7' :
            {'gpio' : 13, 'state' : 0},
    'D8' :
            {'gpio' : 15, 'state' : 0}
}