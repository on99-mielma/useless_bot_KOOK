import random

async def get_random_hex_color():
    r = random.randint(0,16777215)
    hex_r = hex(r)[2:]
    hex_r_6 = hex_r.zfill(6)
    return hex_r_6

def get_random_hex_color_no_await():
    r = random.randint(0,16777215)
    hex_r = hex(r)[2:]
    hex_r_6 = hex_r.zfill(6)
    return hex_r_6