x = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"

def decode(bin):
    output = ''.join(chr(int(bin[i*8:i*8+8], 2)) for i in range(len(bin)//8))
    print(output)
    
decode(x)