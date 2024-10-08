from PIL import Image

def remove_red(image):

    # Convert image to RGB if it's not in that mode
    if image.mode != 'RGB':
        image = image.convert('RGB')


    width, height = image.size
    pixels = image.load()  # Create the pixel map

    for py in range(height):
        for px in range(width):
            #r, g, b = image.getpixel((px, py))
            r, g, b = pixels[px, py]
            tr = 0
            tg = g
            tb = b
            pixels[px, py] = (tr, tg, tb)

    return image

# Example usage
image = Image.open("Che and Jay.png")
nor_image = remove_red(image)
nor_image.save("Che and Jay_without_red.jpg")
