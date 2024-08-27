from PIL import Image, ImageFilter

# Example usage
image = Image.open("Che and Jay.png")
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("Che and Jay_blurred.png")
