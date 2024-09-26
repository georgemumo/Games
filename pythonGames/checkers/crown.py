from PIL import Image, ImageDraw

# Create an empty image with white background
width, height = 44, 25
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define points for the crown
points = [(0, height), (width//4, height//2), (width//2, height), (3*width//4, height//2), (width, height)]

# Draw the crown
draw.polygon(points, fill='gold')

# Save the image
image.save('crown.png')
