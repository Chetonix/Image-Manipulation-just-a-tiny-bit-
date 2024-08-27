from PIL import Image

def apply_gray(image):

    # Convert image to RGB if it's not in that mode
    if image.mode != 'RGB':
        image = image.convert('RGB')


    width, height = image.size
    pixels = image.load()  # Create the pixel map

    for py in range(height):
        for px in range(width):
            #r, g, b = image.getpixel((px, py))
            r, g, b = pixels[px, py]
            tr = r+g+b//3
            tg = r+g+b//3
            tb = r+g+b//3

            pixels[px, py] = (tr, tg, tb)

    return image

# Example usage
image = Image.open("Che and Jay.png")
gray_image = apply_gray(image)
gray_image.save("Che and Jay_gray_1.jpg")
