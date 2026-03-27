from PIL import Image, ImageDraw, ImageFont
import math

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle - pink gradient simulation
    draw.ellipse([0, 0, size-1, size-1], fill='#ff4d94')
    
    # Inner lighter circle
    margin = int(size * 0.08)
    draw.ellipse([margin, margin, size-1-margin, size-1-margin], fill='#ff80b3')
    
    # Draw a flower emoji-like shape
    cx, cy = size // 2, size // 2
    r = int(size * 0.28)
    
    # Petals
    petal_colors = ['#ffffff', '#ffe0ef', '#ffffff', '#ffe0ef', '#ffffff', '#ffe0ef']
    for i in range(6):
        angle = math.radians(i * 60)
        px = cx + int(r * math.cos(angle))
        py = cy + int(r * math.sin(angle))
        pr = int(size * 0.18)
        col = petal_colors[i]
        draw.ellipse([px-pr, py-pr, px+pr, py+pr], fill=col)
    
    # Center
    cr = int(size * 0.14)
    draw.ellipse([cx-cr, cy-cr, cx+cr, cy+cr], fill='#ffdd00')
    draw.ellipse([cx-cr+2, cy-cr+2, cx+cr-2, cy+cr-2], fill='#ffc107')
    
    img.save(filename, 'PNG')
    print(f'Created {filename}')

create_icon(192, '/home/claude/camsnotify/icons/icon-192.png')
create_icon(512, '/home/claude/camsnotify/icons/icon-512.png')
