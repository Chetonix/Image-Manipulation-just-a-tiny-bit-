from PIL import Image

# Open an image file
image = Image.open('Che and Jay.png')

# Convert the image to grayscale
gray_image = image.convert('L')

# Apply a threshold to convert the grayscale image to black and white
threshold = 128
bw_image = gray_image.point(lambda x: 0 if x < threshold else 255, '1')

# Save or display the black and white image
bw_image.save('Che and Jay_black_and_white_filter.png')
