import os
import json
import numpy as np
from PIL import Image

# Directory containing the JSON files
dir_path = './palettes-custom'

# Get the list of JSON files in the directory
json_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.json')]

# Process each file
for json_file in json_files:
    # Full path to the JSON file
    json_file_path = os.path.join(dir_path, json_file)
    
    # Load the JSON file
    with open(json_file_path) as f:
        data = json.load(f)

    # Get the first key in the dictionary as the color palette name
    palette_name = next(iter(data))

    # Extract the colors
    colors = data[palette_name]['colors']

    # Convert color hex values to RGB
    colors_rgb = [tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)) for hex in colors]

    # Create an image using NumPy repetition
    image_data = np.array([colors_rgb]*50)  # 50 is for the height

    # Convert the NumPy array to a PIL image
    img = Image.fromarray(image_data.astype('uint8'), 'RGB')

    # Resize image to be 500x50
    resized_img = img.resize((500,50))

    # Save the image using the name of the JSON file (minus the .json extension)
    output_filename = f"{palette_name}.png"
    output_file_path = os.path.join(dir_path, output_filename)
    resized_img.save(output_file_path)
