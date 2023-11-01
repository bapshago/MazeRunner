from PIL import Image

# Define the colors

B = (0,0,0)
W = (255,255,255)
R = (120,120,120)
# Define the pattern
PATTERN =[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,
          W,W,W,W,W,W,W,W,W,W,W,W,B,W,W,W,W,W,W,W,W,W,W,W,W,]

# Create the image
img = Image.new('RGB', (25, 25), B)
img.putdata(PATTERN)

# Save the image
img.save('cleaner7.png')
