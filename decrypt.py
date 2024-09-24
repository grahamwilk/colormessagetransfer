from PIL import Image
import math


def decrypt(path):
    # find image based on path
    image = Image.open(path)
    width = image.width

    # map the image to pixels
    pixelMap = image.load()
    message_list = []

    # convert x,y and color information to a list
    for x in range(width):
        if x % 12 == 0:
            for y in range(width):
                if y % 12 == 0:
                    for color in range(3):
                        message_list.append(pixelMap[x,y][color])
                    # print(pixelMap[x,y])

    # convert list back into original message
    message_string = ""
    for character in range(len(message_list)):
        message_string += (chr(message_list[character] // 2))
    print("Decrypted message:", message_string)


if __name__ == "__main__":
    decrypt("Abstract.PNG")
