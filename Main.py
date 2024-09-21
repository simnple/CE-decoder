import zlib

customBase85 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%()*+,-./:;=?@[]^_{}'

def Base85ToBin(inputStringBase85):
    global customBase85

    size = len(inputStringBase85)
    bin_data = bytearray()

    i = 0
    while i < size:
        a = (customBase85.index(inputStringBase85[i]) * 85**4)
        i += 1

        if i < size:
            a += (customBase85.index(inputStringBase85[i]) * 85**3)
            i += 1

        if i < size:
            a += (customBase85.index(inputStringBase85[i]) * 85**2)
            i += 1

        if i < size:
            a += (customBase85.index(inputStringBase85[i]) * 85)
            i += 1

        if i < size:
            a += customBase85.index(inputStringBase85[i])
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

    inputStringBase85 = input("Input the text > ")

    bin_data = Base85ToBin(inputStringBase85)

    decompressed_data = zlib.decompress(bin_data)

    with open("output.lua", 'wb') as f:
        f.write(decompressed_data)

    print("Done.")