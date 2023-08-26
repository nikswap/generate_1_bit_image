from PIL import Image
from io import BytesIO
import random

from generate_funk import get_a_funk

W=255
H=255
F=get_a_funk()
print(F)

def f1(x,y):
    return x*y<<2&0xff

def f2(x,y):
    return x*y<<1&0xff
def f3(x,y):
    return x*y&0xff

def f4(x,y):
    return ((x//y*~y)<<3)&0xff

def f5(x,y):
    return ((x//y*~y)<<3)&0xff + ((y//x*~x)<<3)&0xff

def f6(x,y):
    return x*y+~(y//x)

def get_byte_given_index(i):
    x,y=i//H,i%W
    if y == 0:
        y = 1
    if x == 0:
        x = 1
    return int(eval(F))&0xff
    #return ((x//y*~y)<<3)&0xff + ((y//x*~x)<<3)&0xff
    #return random.choice([f1,f2,f3,f4,f5])(x,y)

"""
Cool functions:
    return x*y<<2&0xff
    return x*y<<1&0xff
    return x*y&0xff

    return ((x//y*~y)<<3)&0xff
    y//x-x*x+x//x-x*y//y+y*~y//x*x+~x+y+x-x//~x-y//y+y+y+y+y

"""

data = []
for i in range(H*W):
    val = get_byte_given_index(i)
    data.append(val)

im = Image.frombytes(mode='1', size=(W,H),data=bytes(data))
im.save('test1.png')
