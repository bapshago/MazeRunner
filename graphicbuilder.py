from PIL import Image

# Define the colors
MORTAR = (200, 200, 200)  # Grayish color for the mortar
BRICK = (150, 50, 50)  # Reddish color for the brick
B = (0,0,0)
W = (255,255,255)
R = (120,120,120)
# Define the pattern
PATTERN =[B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,B,W,W,W,W,B,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,W,W,W,W,W,W,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,W,W,W,W,W,W,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,B,B,W,W,B,B,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,W,W,W,W,W,W,W,W,W,W,W,W,W,B,B,B,B,B,B,
          B,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,B,
          B,B,B,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,B,B,B,
          B,B,B,B,B,B,B,B,W,W,W,W,W,W,W,W,W,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,W,W,W,W,W,W,W,W,W,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,W,W,W,W,W,W,W,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,R,R,R,B,R,R,R,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,W,W,W,W,W,W,W,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,W,W,W,W,W,W,W,W,W,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,W,W,W,W,B,B,B,W,W,W,W,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,W,W,W,B,B,B,B,B,W,W,W,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,W,W,W,B,B,B,B,B,W,W,W,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,W,W,W,B,B,B,B,B,W,W,W,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,W,W,W,B,B,B,B,B,W,W,W,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,W,W,W,B,B,B,B,B,W,W,W,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,
          B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]

# Create the image
img = Image.new('RGB', (25, 25), MORTAR)
img.putdata(PATTERN)

# Save the image
img.save('player.png')
