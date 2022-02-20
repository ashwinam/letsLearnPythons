# Scripting with python
# scripting in python means write programme for efficiency or increasing productivity

# Image Pocessing in python
# Image processing is a method to perform some operations on an image, in order to get an enhanced image or to extract some useful information from it. It is a type of signal processing in which input is an image and output may be image or characteristics/features associated with that image.

# In instagram would you believe they post image in original size, No, definitely not because it caused very huge bill, they compressed the image or video

# pillow is the lubrary for image processing in python there is other also there

# --------Developers Fundamentals part vii-------------
# Pick the right library, use the library that are upto date
# Pick the right library is a skill that need to be developed.
# The Best place to learning about library is the official Documentation

# from PIL import Image, ImageFilter

# img = Image.open('Python Scripting/pokemon images/bulbasaur.jpg')
# # print(img) # return PIL object
# print(img.mode)
# print(img.size)
# print(img.format)

# print(dir(img))

# Image filter options
# filtered_image = img.filter(ImageFilter.BLUR)
# filtered_image = img.filter(ImageFilter.SMOOTH)
# filtered_image = img.filter(ImageFilter.SHARPEN)

# filtered_image = img.convert('L')  # grey
# croocked = filtered_image.rotate(360)  # rotate

# resize = croocked.resize((200, 200))

# croped_image = filtered_image.crop((100, 100, 400, 400))

# croped_image.save("Python Scripting/processed images/croped_image.png", 'png')
# # filtered_image.show()


# ------------thumbnail method-----------
# astro_img = Image.open('Python Scripting/astro.jpg')
# print(astro_img.size)  # 5611 x 5339

# resized_astro_img = astro_img.resize((400, 200))
# resized_astro_img.save(
#     "Python Scripting/processed images/resized_astro.png", "png")
# here resize method messed up with the aspect ratio for that there is a thumbnail method it didnt messed up with img aspect ratio

# astro_img.thumbnail((400, 200))
# astro_img.save(
#     "Python Scripting/processed images/thumbnails_astro.png", "png")

# OpenCV
# open cv is a library that helps to process images & videos majorly used in ai/ml.

# ---------PDFs in Python------------
# we have 3 pdf

import PyPDF2

# open the pdf file in read binary format
with open("Python Scripting/pdf/dummy.pdf", 'rb') as file:
    # print(file.read()) error
    reader = PyPDF2.PdfFileReader(file)  # grab the file
    # print(reader.getNumPages()) # page number
    page = reader.getPage(0)  # grab the page
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()  # writer object
    writer.addPage(page)  # insert the modified page to the object
    with open("Python Scripting/pdf/tilt.pdf", 'wb') as new_file:
        writer.write(new_file)  # create modified pdf
