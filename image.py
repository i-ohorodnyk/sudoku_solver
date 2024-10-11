from PIL import Image, ImageDraw, ImageFont
from main import get_field

# create an image
out = Image.new("RGB", (500, 500), (255, 255, 255))

# get a font
fnt = ImageFont.truetype("SixtyfourConvergence.ttf", 50)
# get a drawing context
d = ImageDraw.Draw(out)

field = get_field()

# draw multiline text
d.multiline_text((10, 10), '\n'.join([''.join([str(i) for i in row]) for row in field]), font=fnt, fill=(0, 0, 0))

out.save("img.png")
