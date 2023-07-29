#   Simple code for alternate LED blinking
MEMSIZE = 0x8000
code = bytearray([
    0xea
    ] * 10)

# rom = code + bytearray([0xea] * (1024 - len(code)))

#   Swap the code from below if you want to have full ROM
#   for your first programming.
#   Otherwise I suggest programming only 1024 bytes to make it faster
#   Full 32KB takes over 5 minutes!


rom = code + bytearray([0xea] * (MEMSIZE - len(code)))
rom[0x7ffc] = 0x00
rom[0x7ffd] = 0x80

with open("rom.bin", "wb") as out_file:
    out_file.write(rom)
    print("Done")