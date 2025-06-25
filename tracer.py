from PIL import Image, ImageDraw, ImageFont

def create_tracing_image(input_text):
    # Determine image size based on text
    font_size = 100
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    temp_image = Image.new("RGB", (1, 1), "white")
    temp_draw = ImageDraw.Draw(temp_image)
    text_width, text_height = temp_draw.textbbox((0, 0), input_text, font=font)[2:]

    width = text_width + 100  # Padding for spacing
    height = text_height + 100
    
    # Create a blank white image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw text with stroke for better visibility
    draw.text(
        (text_x, text_y), input_text, font=font, fill="lightgray",
        stroke_width=3, stroke_fill="black"
    )

    image.save(save)
    print("image trace was saved as",save)

words = input("Enter the text you want to trace: ")
save=input("How would you like to save this: ")
create_tracing_image(words)
