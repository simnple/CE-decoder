import zlib
import sys

custom_base85_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%()*+,-./:;=?@[]^_{}"

def base85_to_bin(bin_value: str):
    size = len(bin_value)
    bin_data = bytearray()

    i = 0
    while i < size:
        a = (custom_base85_chars.index(bin_value[i]) * 85**4)
        i += 1

        if i < size:
            a += (custom_base85_chars.index(bin_value[i]) * 85**3)
            i += 1

        if i < size:
            a += (custom_base85_chars.index(bin_value[i]) * 85**2)
            i += 1

        if i < size:
            a += (custom_base85_chars.index(bin_value[i]) * 85)
            i += 1

        if i < size:
            a += custom_base85_chars.index(bin_value[i])
            i += 1

            bin_data.extend([
                (a >> 24) & 0xFF,
                (a >> 16) & 0xFF,
                (a >> 8) & 0xFF,
                a & 0xFF
            ])

    remainder = size % 5
    if remainder == 2:
        a += 84 * 85**2 + 84 * 85 + 84
        bin_data.extend([
            (a >> 24) & 0xFF
        ])

    elif remainder == 3:
        a += 84 * 85 + 84
        bin_data.extend([
            (a >> 24) & 0xFF,
            (a >> 16) & 0xFF
        ])

    elif remainder == 4:
        a += 84
        bin_data.extend([
            (a >> 24) & 0xFF,
            (a >> 16) & 0xFF,
            (a >> 8) & 0xFF
        ])

    return bin_data

if __name__ == "__main__":
    bin_value = open(sys.argv[1], "r").read()

    bin_data = base85_to_bin(bin_value)
    decompressed_data = zlib.decompress(bin_data)

    open("result.lua", "wb").write(decompressed_data)
