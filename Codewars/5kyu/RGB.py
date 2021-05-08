"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

def help(c):
    if c < 0:
        return 0
    if c > 255:
        return 255
    return c
def hex_conversion(c):
    var = str(hex(c))
    if len(var) == 3:
        return '0' + var[2:]
    else:
        return var[2:]

def rgb(r, g, b):
    r = help(r)
    g = help(g)
    b = help(b)
    return hex_conversion(r).upper() + hex_conversion(g).upper() + hex_conversion(b).upper()

print(rgb(-20,275,125))