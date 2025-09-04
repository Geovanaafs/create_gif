# Import required libraries
# - imageio.v3 (aliased as iio) for reading and writing images
# - os for working with file paths and directories
import imageio.v3 as iio
import os

# Define the folder where the images are stored
image_folder = '/images'

# Get a list of all files in the folder (useful for checking what’s inside)
files = os.listdir(image_folder)
print("Files in folder:", files)

# Build the sequence of filenames for the GIF:
# Forward: cat1.png → cat7.png
# Backward: cat6.png → cat2.png
filenames = [f"cat{i}.png" for i in list(range(1, 8)) + list(range(6, 1, -1))]
print("GIF sequence:", filenames)

# Prepare a list to hold the loaded images
images = []

# Loop through each filename, load the image, and add it to the list
# Use os.path.join() to create the full path to each image
for filename in filenames:
    filepath = os.path.join(image_folder, filename)  # full path
    images.append(iio.imread(filepath))

# Save the images as an animated GIF
# - duration=500 → each frame is displayed for 500 ms
# - loop=0 → the GIF repeats forever
iio.imwrite('cat.gif', images, format='GIF', duration=500, loop=0)

print("GIF created successfully: cat.gif")

