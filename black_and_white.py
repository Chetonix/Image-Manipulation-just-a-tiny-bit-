from PIL import Image

def apply_black_white(image):

    # Convert image to RGB if it's not in that mode
    if image.mode != 'RGB':
        image = image.convert('RGB')


    width, height = image.size
    pixels = image.load()  # Create the pixel map

    for py in range(height):
        for px in range(width):
            #r, g, b = image.getpixel((px, py))
            r, g, b = pixels[px, py]
            avg = r+g+b//3
            

            if avg > 128:
                tr,tg,tb = 255, 255, 255
            else:
                tr, tg, tb = 0, 0, 0
            pixels[px, py] = (tr, tg, tb)

    return image

# Example usage
image = Image.open("Che and Jay.png")
gray_image = apply_black_white(image)
gray_image.save("Che and Jay_black_and_white_1.jpg")
