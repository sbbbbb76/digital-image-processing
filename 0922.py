from math import ceil


def hexdump(file,num):
    # f = open(file)
    f = open(file, 'rb')  # debug
    h = f.read(num)

    # all the bytes as 2 character hex strings
    # hl = [hex(ord(c))[2:].zfill(2) for c in h]
    hl = [hex(c)[2:].zfill(2) for c in h]  # debug

    # fill up to a multiple of width 16
    hl2 = hl +(-len(hl)%16)*['  ']
    asc = ['.']*num

    # creates ascii values (if printable) of bytes
    for i in range(num):
        ii = int(hl[i],16)
        if ii>=32 and ii<=126:
            asc[i] = chr(ii)

    # fill up to a multiple of width 16
    asc = asc + (-len(hl)%16)*[' ']

    for n in range(int(ceil(num/16.0))):
        print(hex(n*16)[2:].zfill(6)+': ',
              ' '.join([hl2[16*n+2*i]+hl2[16*n+2*i+1] for i in range(8)]),
              '|'+''.join([asc[16*n+i] for i in range(16)])+'|')
        
hexdump(r'C:\Users\CJCU\Desktop\backyard.png', 64)
print()
hexdump(r'C:\Users\CJCU\Desktop\emu.tif', 64)
