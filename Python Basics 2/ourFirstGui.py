# statement
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# 1 iterate over a picture
  # if 0 -> print ' '
  # if 1 -> print '*'
fill = '#'
empty = ' '
for row in picture:
  for pixel in row:
    if pixel:
      print(fill, end='')
    else:
      print(empty, end='')
  print()