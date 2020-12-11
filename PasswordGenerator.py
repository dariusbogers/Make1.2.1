
import random

def genbyte():
    temp = ""
    for y in range(8):
        i = round(random.random())
        temp = temp + str(i)

    while 0 <= int(temp, 2) <= 32:
        temp = genbyte()

    while 126 <= int(temp, 2):
        temp = genbyte()

    while int(temp, 2) == 94:
        temp = genbyte()

    while int(temp, 2) == 96:
        temp = genbyte()

    return temp

def genpwd(bitL):
    pwd = ""
    byteL = int(bitL / 8)
    for x in range(byteL):
        pwd = pwd + chr(int(genbyte(), 2))
    return pwd
