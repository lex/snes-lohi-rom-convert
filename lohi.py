import sys


def lo_hi_rom_convert(in_file_path, out_file_path):
    try:
        with open(in_file_path, "rb") as in_file:
            l_file = in_file.read()
        o_file = bytearray(len(l_file) * 2)
        div = 0x8000
        pcs = len(l_file) // div
        hi_rom_pos = 0
        pc_pos = 0
        for c in range(pcs):
            for d in range(div):
                pc_pos = d + (c * div)
                hi_rom_pos = d + (c * 0x10000)
                o_file[hi_rom_pos] = l_file[pc_pos] if c != 0 else 0xFF
                o_file[hi_rom_pos + div] = l_file[pc_pos]
        with open(out_file_path, "wb") as out_file:
            out_file.write(o_file)
    except Exception as ex:
        print_usage()
        print(f"Error: {ex}")


def print_usage():
    print("Usage: python3 lohi.py [in_file_path] [out_file_path]")


def main():
    if len(sys.argv) != 3:
        print_usage()
    else:
        in_file_path = sys.argv[1]
        out_file_path = sys.argv[2]
        lo_hi_rom_convert(in_file_path, out_file_path)


if __name__ == "__main__":
    main()
