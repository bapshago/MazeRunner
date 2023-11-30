from PIL import Image

# Define the colors

B = (0,0,0)
W = (255,255,255)
R = (120,120,120)
# Define the pattern
PATTERN =[B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,B,B,B,B,W,W,B,B,B,B,B,W,B,W,W,W,W,W,W,W,W,B,B,
          B,W,B,W,W,W,B,W,B,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,B,
          B,W,B,W,W,W,B,W,B,B,B,W,W,W,B,W,W,W,W,W,B,B,B,W,B,
          B,W,B,W,W,W,B,W,B,B,B,W,W,W,B,W,W,W,W,W,W,W,W,W,B,
          B,W,B,W,W,W,B,W,B,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,B,
          B,W,B,B,B,B,W,W,B,B,B,B,B,W,B,B,B,B,B,W,W,W,W,W,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,B,B,B,B,W,B,W,W,B,W,B,B,B,B,W,B,B,B,B,B,W,B,B,
          B,W,B,W,W,W,W,B,W,W,B,W,B,W,W,W,W,W,W,B,W,W,W,W,B,
          B,W,B,W,W,W,W,B,W,W,B,W,B,B,B,W,W,W,W,B,W,W,W,B,B,
          B,W,B,W,W,W,W,B,W,W,B,W,W,W,W,B,W,W,W,B,W,W,W,W,B,
          B,W,B,B,B,B,W,B,B,B,B,W,B,B,B,B,W,W,W,B,W,W,W,B,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W,W,B,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,B,
          B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,
          B,W,B,W,B,W,B,W,B,W,B,W,B,W,B,W,B,W,B,W,B,W,B,B,B,
          B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,]

# Create the image
img = Image.new('RGB', (25, 25), B)
img.putdata(PATTERN)

print(img)
#Save the image
img.save('delcustbtn.png')
