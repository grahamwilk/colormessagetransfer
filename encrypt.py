from PIL import Image
import math

def encrypt(message):
    chars = []
    for char in message:
        chars.append(ord(char))
    math.ceil(len(chars)/3)

    print("this message is very encrypted")
