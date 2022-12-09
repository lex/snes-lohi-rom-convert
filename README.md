# snes-lohi-rom-convert

This project provides a Python script that converts ROM images between the HiROM and LoROM formats used by the Super Nintendo Entertainment System (SNES).

## Background

The SNES is a video game console released by Nintendo in 1990. It uses a custom microprocessor, the Ricoh 5A22, which is based on the 16-bit WDC 65C816 CPU. The 5A22 has a 24-bit address bus, which allows it to address up to 16 MB of memory.

However, the SNES cartridge ROMs typically have a size of 1 MB (LoROM) or 2 MB (HiROM), and use a different addressing scheme than the 5A22 CPU. In LoROM, the first 64 KB of the cartridge ROM is mapped to the first 64 KB of the CPU address space, and the remaining 960 KB is mapped to the second 64 KB of the CPU address space, at addresses 0x8000-0xFFFF. In HiROM, the first 64 KB of the cartridge ROM is mapped to the second 64 KB of the CPU address space, at addresses 0x8000-0xFFFF, and the remaining 1.9 MB is mapped to the first 64 KB of the CPU address space.

This addressing scheme allows the SNES to access the cartridge ROM in a way that is compatible with the 5A22 CPU, and enables the ROM to use the full address space of the CPU. However, it also means that the ROM must be converted between the LoROM and HiROM formats depending on the mapping used by the SNES.

## Usage

To use the `lohi.py` script, you need to have Python 3 installed on your computer. You can then run the script with the following command:

```sh
$ python3 lohi.py [in_file_path] [out_file_path] [conversion_type]
```

where

- `[in_file_path]` is the path to the input ROM image
- `[out_file_path]` is the path to the output ROM image
- `[conversion_type]` is the type of conversion to perform

The `[conversion_type]` can be one of the following strings:

- `lo-to-hi`: convert a LoROM image to a HiROM image.
- `hi-to-lo`: convert a HiROM image to a LoROM image.

For example, to convert a LoROM image at `in.rom` to a HiROM image and save it to `out.rom`, you can run the following command:

```sh
$ python3 lohi.py in.rom out.rom lo-to-hi
```

This command converts the LoROM image at `in.rom` to a HiROM image and saves it to `out.rom`.

## Requirements

snes-lohi-rom-convert requires Python 3.x to run. It has been tested with Python 3.8, but should also work with other versions of Python 3.x.

## License

snes-lohi-rom-convert is licensed under the BSD-3 License. See the [LICENSE](LICENSE) file for more details.
