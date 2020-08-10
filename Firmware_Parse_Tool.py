#!/usr/bin/python3
#
# Firmware_Parse_Tool.py
# Parse binary file to remove 5 byte programming header and 1 byte checksum footer 
# from every 1030 bytes
# Usage:
# ./Firmware_Parse_Tool.py input_file output_file block_size header_size
#
# Ex: Yaesu Main Firmware
# ./Firmware_Parse_Tool.py USB_Capture.bin outfile.bin 1030 5
#
# Ex: Kenwood Firmware Update Capture
# ./Firmware_Parse_Tool.py USB_Capture.bin outfile.bin 1041 16

import sys
with open(sys.argv[1], "rb") as binary_file:
    binary_file.seek(0, 2)                          # Seek to the end.
    num_bytes = binary_file.tell()                  # Get the file size.

    block_count = 0                                 # keep track of the block we are on.
    block_size = int(sys.argv[3])                   # size of each block captured.
    data_size = 1024                                # so far this has been 1024.
    header_size = int(sys.argv[4])                  # number of header bytes.
    num_blocks = int (num_bytes / block_size)

    for i in range(num_blocks):
        binary_file.seek( (i * block_size) + header_size )
        data_bytes = binary_file.read(data_size)
        with open(sys.argv[2], "ab") as outfile:
            outfile.write(data_bytes)
