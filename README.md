# snes-lohi-rom-convert

snes-lohi-rom-convert is a simple command-line tool that allows you to convert SNES ROMs from LoROM format to HiROM format.

Based on [LoHiROM](https://github.com/danielburgess/LoHiROM) by [danielburgess](https://github.com/danielburgess).

## Background

The Super Nintendo Entertainment System (SNES) uses two different memory addressing schemes for its ROMs: LoROM and HiROM. LoROM uses a 24-bit address space, which allows it to access up to 16 MB of ROM data. HiROM, on the other hand, uses a 32-bit address space, which allows it to access up to 4 GB of ROM data.

LoROM and HiROM have different advantages and disadvantages. LoROM is generally considered to be faster than HiROM, but it has a limited address space, which can be a problem for larger games. HiROM, on the other hand, has a much larger address space, which allows it to accommodate larger games, but it is generally slower than LoROM.

## Usage

To use snes-lohi-rom-convert, open a terminal and navigate to the directory where lohi.py is located. Then, run the following command:

```sh
python3 lohi.py [in_file_path] [out_file_path]
```

where `[in_file_path]` is the path to the input LoROM file and `[out_file_path]` is the path where the converted HiROM file should be saved.

For example, if the input LoROM file is located at `/home/user/roms/input.smc` and you want to save the converted HiROM file at `/home/user/roms/output.smc`, you would run the following command:

```sh
python3 lohi.py /home/user/roms/input.smc /home/user/roms/output.smc
```

## Requirements

snes-lohi-rom-convert requires Python 3.x to run. It has been tested with Python 3.8, but should also work with other versions of Python 3.x.

## License

snes-lohi-rom-convert is licensed under the BSD-3 License. See the [LICENSE](LICENSE) file for more details.
