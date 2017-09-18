import os
from PIL import Image, ImageDraw, ImageFont
barcode_folder_path = os.path.join(os.getcwd(), "barcodes")
barcode_file_format = ".png"

if not os.path.exists(barcode_folder_path):
    os.makedirs(barcode_folder_path)

typefaces = ["CarolinaBarUPC_Normal.ttf", "salvagetag.ttf"]
typeface = ImageFont.truetype("fonts/"+typefaces[0], 100)

upc_conversion_table = {
        "manufacturer-number": {
            "1": "q", "2": "w", "3": "e", "4": "r", "5": "t",
            "6": "y", "7": "u", "8": "i", "9": "o", "0": "p"
         },
        "product-code": {
            "1": "a", "2": "s", "3": "d", "4": "f", "5": "g",
            "6": "h", "7": "j", "8": "k", "9": "l", "0": ";"
        },
        "check-digit": {
            "1": "z", "2": "x", "3": "c", "4": "v", "5": "b",
            "6": "n", "7": "m", "8": ",", "9": ".", "0": "/"
        }
}


class Barcode:
    barcode_width, barcode_height = 555, 205

    # Update: forces a an overwrite of the specified barcode
    def __init__(self, upc, update=True, info=False):
        self.upc = upc
        self.path = os.path.join(barcode_folder_path, "".join([self.upc, barcode_file_format]))
        self.barcode_text = convert_to_barcode_text(upc)
        created_barcode = False

        if not os.path.isfile(self.path) or update:
            self.create_barcode_image()
            created_barcode = True
        if info:
            print(self.upc, self.path, self.barcode_text, "Made Barcode: ", created_barcode)

    def image(self):
        with Image.open(self.path) as im:
            return im

    def change_size(self, width, height):
        self.barcode_width = width
        self.barcode_height = height

    def create_barcode_image(self, info=True):
        width, height = [self.barcode_width, self.barcode_height]
        image = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(image)
        draw.text((5, 2), self.barcode_text, font=typeface, fill="black")
        if info:
            print("Rendered: ", self.barcode_text, "from", self.upc )
            image.show()

        image.save(self.path)

def convert_to_salvage_barcode(code):
    start = "ì"
    end = "î"
    converted_code = "".join(())


def salvage_checksum(code):
    value = {
        "0": 16,
        "1": 17,
        "2": 18,
        "3": 19,
        "4": 20,
        "5": 21,
        "6": 22,
        "7": 23,
        "8": 24,
        "9": 25,
    }

    start = 105
    num = 1
    for i in code:
        start += value[i] * num
        num += 1
    print(start/103)




def convert_to_barcode_text(upc):
    # First Digit
    upc_swap = upc[:1]

    # Next 5 Digits
    for num in upc[1:6]:
        upc_swap += upc_conversion_table["manufacturer-number"][num]

    # Add Center Guard Bars
    upc_swap += "-"

    # Last 5 Digits
    for num in upc[6:11]:
        upc_swap += upc_conversion_table["product-code"][num]

    # Twelfth and Final Digit
    for num in upc[11:]:
        upc_swap += upc_conversion_table["check-digit"][num]

    return upc_swap

if __name__ == "__main__":
    # barcode = Barcode("999999999999")
    salvage_checksum("9449")
