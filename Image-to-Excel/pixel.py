from PIL import Image

image_name = "Cloud"
file = open("{0}.csv".format(image_name), "w")
im = Image.open("{0}.jpg".format(image_name))
width, height = im.size

for y in range(height):
	file.write("\n")
	for x in range(width):
		RGB_im = im.convert("RGB")
		r, g, b = RGB_im.getpixel((x, y))
		file.write("{0} {1} {2},".format(str(r), str(g), str(b)))

file.close()
