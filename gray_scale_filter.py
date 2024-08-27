from PIL import Image

# Open an image file
image = Image.open('Che and Jay.png')

# Convert the image to grayscale
gray_image = image.convert('L')

# Save or display the grayscale image
gray_image.save('Che and Jay_gray_scale_filter.png')
