#!/usr/bin/python3
import serial
import time
import os
import sys
import argparse




def main():
    write()
    read()

    F.close()
    ser.close()


def read():
    # Reads file and saves, showing what has came back
    D = open(out_file, "wb")
    val = ser.read(fileSize * 256)
    D.write(val)
    print(f"Recieved {len(val)} bytes")
    print(bytes(val).hex(), end=' ')
    D.close()


def write():
    # Sends file size and prints to confirm
    ser.write((fileSize).to_bytes(1, 'big'))
    print(f"Sending {256 * int.from_bytes(ser.read(), 'big')} bytes ...")
    time.sleep(1)
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    # Sends file in 1024 byte chunks
    toSend = F.read(1024)
    while toSend:
        ser.write(bytearray(toSend))
        print(bytes(toSend).hex())
        print(int(ser.readline()))
        toSend = F.read(1024)

    ser.reset_input_buffer()
    ser.reset_output_buffer()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--PORT', help='Device Port', required=True)
    parser.add_argument('-b', '--BAUD', help='Baudrate', default=9600, required=False)
    parser.add_argument('-f', '--FILE', help='Input Binary File', required=True)
    parser.add_argument('-o', '--OUTPUT', help='Output Binary File', required=False, default='out.bin')

    args = parser.parse_args()

    port = args.PORT
    baud = args.BAUD
    in_file = args.FILE
    out_file = args.OUTPUT
    # '/dev/ttyACM0'
    # Opens com port and bin file to be read
    ser = serial.Serial(port, baudrate=baud, timeout=None)
    F = open(in_file, "rb")
    # Saves fileSize as int that fits into a byte
    fileSize = int(os.path.getsize(in_file) / 256)

    # Wait for Arduino
    time.sleep(2)
    main()