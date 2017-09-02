import numpy
import PIL.Image

# Convert Image to array
img = PIL.Image.open("monkey.jpg").convert("L")
arr = numpy.array(img)

# Convert array to Image
img = PIL.Image.fromarray(arr)