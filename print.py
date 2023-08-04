# from escpos import *
# x = printer.Usb(0x28e9,0x0289,0,0x98,0x02)  # replace with your own printer's vendor and product id
# # Print text
# x.text("Hello World\n")
# Print image
# x.image("logo.gif")
# Print QR Code
# x.qr("You can readme from your smartphone")
# # Print barcode
# x.barcode('1324354657687','EAN13',64,2,'','')
# # Cut paper
# x.cut()
import serial

ser = serial.Serial('COM18', 9600) # open COM18 port with baud rate of 9600
ser.write(b'Hello World this is a test\n') # send the string "Hello World" over the serial connection
ser.close() # close the serial connection


# print_big_text('Hello World')
# print_big_text('Hello World')
ser = serial.Serial('COM18', 9600) # open COM18 port with baud rate of 9600
for n in range(10):
    
    ser.write(b"1234 ^^^^^\n") # send the string "Hello World" over the serial connection
    # print_big_text(str(n))



n = 5 # set the size of the diamond


ser.write(b"     #     \n") # send the string "Hello World" over the serial connection
ser.write(b"    ###    \n") # send the string "Hello World" over the serial connection
ser.write(b"   #####   \n") # send the string "Hello World" over the serial connection
ser.write(b"  #######  \n") # send the string "Hello World" over the serial connection
ser.write(b" ######### \n") # send the string "Hello World" over the serial connection
ser.write(b"###########\n") # send the string "Hello World" over the serial connection
ser.write(b" ######### \n") # send the string "Hello World" over the serial connection
ser.write(b"  #######  \n") # send the string "Hello World" over the serial connection
ser.write(b"   #####   \n") # send the string "Hello World" over the serial connection
ser.write(b"    ###    \n") # send the string "Hello World" over the serial connection
ser.write(b"     #     \n") # send the string "Hello World" over the serial connection


ser.close() # close the serial connection


