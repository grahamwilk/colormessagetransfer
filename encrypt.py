from PIL import Image
import math

def encrypt(message):
    pixelCount = math.ceil(len(message)/3)
    length = math.ceil(math.sqrt(pixelCount))
    chars = []
    for char in message:
        chars.append(ord(char))
    while length**2 > len(chars)/3:
        chars.append(32)

    image = Image.new(mode="RGB", size=(length, length))
    pixelMap = image.load()

    k = 0
    for i in range(length):
        for j in range(length):
            pixelMap[i,j] = (chars[k]*2, chars[k+1]*2, chars[k+2]*2)

            k = k+3
            print(pixelMap[i,j])

    # Scale the image by 12x
    new_size = (length * 12, length * 12)
    scaled_image = image.resize(new_size, Image.NEAREST)

    scaled_image.show()
    print("this message is very encrypted yes very nice yes")

encrypt("Abstract Most modern encryption methods, like the RSA algorithm, rely on the fact that it would take a hacker an unreasonable amount of time and computing power to decrypt a message without knowing the private key. At the same time, computer technology is advancing every year. Encryption methods that were good enough at one time can now be brute forced in a reasonable amount of time with a fast computer. The weakness of a widely available encryption method is that people will be able to figure out how it works. This project aims to create a way to encrypt a message in a colorful image that won’t mean anything to those who don’t know what it is. Problem Identification The problem is that data being sent over the internet can often be intercepted by hackers through a variety of means. For hackers which are trying to intercept passwords, they will often be looking for encrypted values which they can try to crack. By sending a colorful image instead of plain encrypted text, it could be possible to get around hackers who are clueless about what the purpose the image serves, since it is just a batch of colorful pixels. In short, we are creating a unique encryption model that instead of sending encrypted text, sends an encrypted image. The recipient could then use image data to recreate the message by reversing the process. Objective Our goal is to create a program which takes your message and converts it into colorful pixels. This is done by first converting each character to its extended ASCII index. We will then use those numbers in sets of 3 to create a colorful pixel, with each number corresponding to the red, green, and blue values of the pixel. After that, we will add each pixel one by one to a square image (if there are not enough index values to fill up a square, we will add the value 32, signifying a space, until it is full) and send that image to our recipient. The recipient can then work backwards, taking the pixels and converting them back into their ASCII indexes, and then back into plain text. The datasets we will use are the extended ASCII library, along with a dataset including hundreds of ASCII messages so we can test the efficiency of our encryption model.")
