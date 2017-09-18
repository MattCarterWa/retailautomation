from PIL import Image, ImageDraw
class Barcode:
    width = 5
    height = 30
    size = (width, height)
    whitespace = 60

    def __init__(self):
        pass

test_code = "11010000100110001010001100010001010111011110100010110001110001011011000010100100001011001100011101011"


bar = Barcode
im_size = (bar.width * len(test_code) + bar.whitespace * 2, 60)
im = Image.new("RGB", im_size, "white")
# im.show()
for l in test_code:
    print(l)

    if l:
        print(l)


