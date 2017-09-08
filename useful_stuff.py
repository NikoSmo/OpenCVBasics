<<<<<<< HEAD
import numpy
import PIL.Image

# Convert Image to array
img = PIL.Image.open("monkey.jpg").convert("L")
arr = numpy.array(img)

# Convert array to Image
=======
import numpy
import PIL.Image

# Convert Image to array
img = PIL.Image.open("monkey.jpg").convert("L")
arr = numpy.array(img)

# Convert array to Image
>>>>>>> dc7611aca7c2710ead5786e72c89bb64bd477149
img = PIL.Image.fromarray(arr)