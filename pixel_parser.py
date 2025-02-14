import re
from PIL import Image
import numpy as np

# Load existing canvas or create new (100x100 grid)
try:
    img = Image.open("canvas.png")
    pixels = np.array(img)
except:
    pixels = np.zeros((100, 100, 3), dtype=np.uint8) + 255  # White canvas

# Parse latest commit message for pixel data
commit_message = os.getenv("COMMIT_MESSAGE")  # From GitHub context
match = re.search(r"pixel\((\d+),(\d+),#([0-9a-fA-F]{6})\)", commit_message)

if match:
    x, y, color = match.groups()
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    pixels[int(y), int(x)] = [r, g, b]

# Save updated canvas
Image.fromarray(pixels).save("canvas.png")