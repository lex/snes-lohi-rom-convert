import sys


def lo_hi_rom_convert(in_file_path, out_file_path):
    # Open the input file in binary mode and read its content
    with open(in_file_path, "rb") as in_file:
        lo_rom = in_file.read()

    # Check if the input ROM image is a valid LoROM image
    if len(lo_rom) != 0x100000 or lo_rom[0x7FD5] != 0x20:
        raise ValueError("Input ROM image is not a valid LoROM image")

    # Create an empty HiROM image with twice the size of the input LoROM image
    hi_rom = bytearray(len(lo_rom) * 2)

    # Copy the first 64 KB of the LoROM image to the HiROM image
    hi_rom[:0x10000] = lo_rom[:0x10000]

    # Copy the remaining data from the LoROM image to the HiROM image,
    # doubling each byte
    for i in range(0x10000, len(lo_rom)):
        hi_rom[i * 2] = lo_rom[i]
        hi_rom[i * 2 + 1] = lo_rom[i]

    # Set the ROM type in the HiROM image header to 0x21 (HiROM)
    hi_rom[0x7FD5] = 0x21

    # Open the output file in binary mode and write the content of the HiROM image
    with open(out_file_path, "wb") as out_file:
        out_file.write(hi_rom)


def hi_lo_rom_convert(in_file_path, out_file_path):
    # Open the input file in binary mode and read its content
    with open(in_file_path, "rb") as in_file:
        hi_rom = in_file.read()

    # Check if the input ROM image is a valid HiROM image
    if len(hi_rom) != 0x200000 or hi_rom[0x7FD5] != 0x21:
        raise ValueError("Input ROM image is not a valid HiROM image")

    # Create an empty LoROM image with half the size of the input HiROM image
    lo_rom = bytearray(len(hi_rom) // 2)

    # Copy the first 64 KB of the HiROM image to the LoROM image
    lo_rom[:0x10000] = hi_rom[:0x10000]

    # Copy the remaining data from the HiROM image to the LoROM image,
    # averaging the data from each pair of bytes
    for i in range(0x10000, len(lo_rom)):
        lo_rom[i] = (hi_rom[i * 2] + hi_rom[i * 2 + 1]) // 2

    # Set the ROM type in the LoROM image header to 0x20 (LoROM)
    lo_rom[0x7FD5] = 0x20

    # Open the output file in binary mode and write the content of the LoROM image
    with open(out_file_path, "wb") as out_file:
        out_file.write(lo_rom)


def main():
    # Check if the correct number of command-line arguments were provided
    if len(sys.argv) != 4:
        print(
            "Usage: python3 lohi.py [in_file_path] [out_file_path] [conversion_type]")
        return

    # Get the input and output file paths and the conversion type from the command-line arguments
    in_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    conversion_type = sys.argv[3]

    # Convert the input ROM image to a HiROM image if the conversion type is "lo-to-hi"
    if conversion_type == "lo-to-hi":
        lo_hi_rom_convert(in_file_path, out_file_path)

    # Convert the input ROM image to a LoROM image if the conversion type is "hi-to-lo"
    elif conversion_type == "hi-to-lo":
        hi_lo_rom_convert(in_file_path, out_file_path)

    # Print an error message if the conversion type is not "lo-to-hi" or "hi-to-lo"
    else:
        print("Error: Invalid conversion type. Must be 'lo-to-hi' or 'hi-to-lo'.")


if __name__ == "__main__":
    main()
