import imageio.v3 as iio


filenames = ['cat1.png','cat2.png','cat3.png', 'cat4.png', 'cat5.png', 'cat6.png', 'cat7.png','cat6.png','cat5.png', 'cat4.png','cat3.png','cat2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('cat.gif', images, duration = 500, loop = 0)
# iio.imwrite('team.gif', images, duration = 500, loop = 0)