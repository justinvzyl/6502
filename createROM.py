import time

import serial


PORT = '/dev/ttyACM0'
BAUD = 57600
MEMSIZE = 32768

def make_rom():
    rom = bytearray([0xea] * MEMSIZE)
    with open('rom.bin', 'wb') as out_file:
        out_file.write(rom)

def send_rom(ser: serial.Serial):
    with open('rom.bin', 'rb') as in_file:
        b = in_file.read()
        for a in b:
            ser.write(a)
            time.sleep(0.01)
            print(a)

if __name__ == '__main__':
    ser = serial.Serial(port=PORT, baudrate=BAUD)
    make_rom()
    send_rom(ser)


