from PIL import Image, ImageDraw

def create_spaceship_image():
    width, height = 64, 64
    spaceship_image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(spaceship_image)

    # Draw a simple spaceship (triangle shape)
    draw.polygon([(width / 2, 0), (width, height), (0, height)], fill="blue", outline="white")
    draw.rectangle([width / 4, height * 0.8, width * 0.75, height], fill="blue", outline="white")

    spaceship_image.save("spaceship.png")

def create_alien_image():
    width, height = 64, 64
    alien_image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(alien_image)

    # Draw a simple alien (square with eyes)
    draw.rectangle([10, 10, width - 10, height - 10], fill="green", outline="white")
    draw.ellipse([20, 20, 30, 30], fill="white")
    draw.ellipse([width - 30, 20, width - 20, 30], fill="white")

    alien_image.save("alien.png")

def create_bullet_image():
    width, height = 5, 10
    bullet_image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(bullet_image)

    # Draw a simple bullet (rectangle shape)
    draw.rectangle([0, 0, width, height], fill="red", outline="black")

    bullet_image.save("bullet.png")

if __name__ == "__main__":
    create_spaceship_image()
    create_alien_image()
    create_bullet_image()
