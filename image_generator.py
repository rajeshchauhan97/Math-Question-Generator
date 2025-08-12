import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_image(description, output_path, size=(800, 600)):
    """Create a simple placeholder image with description."""
    print(f"Image generation via Gemini is not directly supported via this method. Using placeholder...")
    img = Image.new('RGB', size, color=(240, 240, 240))
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([(10, 10), (size[0]-10, size[1]-10)], outline=(200, 200, 200), width=2)
    
    # Add title
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    draw.text((20, 20), "Placeholder Image", fill=(0, 0, 0), font=font)
    
    # Add description
    desc_lines = [description[i:i+50] for i in range(0, min(len(description), 150), 50)]
    for i, line in enumerate(desc_lines):
        draw.text((20, 70 + i*30), line, fill=(100, 100, 100), font=ImageFont.load_default())
    
    # Add simple diagram based on content
    if "ball" in description.lower() or "sphere" in description.lower() or "circles" in description.lower():
        radius = 30
        positions = [(150, 200), (300, 200), (450, 200), (225, 300), (375, 300)]
        for x, y in positions:
            draw.ellipse([(x-radius, y-radius), (x+radius, y+radius)], outline=(0, 0, 255), width=2)
    else:
        draw.rectangle([(100, 150), (700, 450)], outline=(0, 0, 0), width=2)
    
    img.save(output_path)
    print(f"Placeholder image saved at {output_path}")