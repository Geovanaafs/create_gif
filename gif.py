# Import the imageio.v3 library as iio for reading/writing images
import imageio.v3 as iio  

# List of image file names to be combined into a GIF
filenames = ['cat1.png','cat2.png','cat3.png', 'cat4.png', 'cat5.png', 'cat6.png', 'cat7.png',
             'cat6.png','cat5.png', 'cat4.png','cat3.png','cat2.png']

# Create an empty list to store the loaded images
images = []

# Loop through each file name, read the image, and add it to the images list
for filename in filenames:
    images.append(iio.imread(filename))

# Write the images to a GIF file
# duration = 500 sets the time (in milliseconds) each frame is displayed
# loop = 0 makes the GIF loop forever
iio.imwrite('cat.gif', images, duration=500, loop=0)
