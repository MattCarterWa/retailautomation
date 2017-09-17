from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# Gets date info
month = str(datetime.today().month)
if len(month) == 1:
    month = "0" + month
date = str(datetime.today().day)
if len(date) == 1:
    date = "0" + date
year = str(datetime.today().year)

# Store info here
division = "701"
store = "00688"
div_string = "".join(("Division: ", division))
store_string = "".join(("Store #: ", store))
date_string = "".join(("Date: ", "/".join((month, date, year))))

# Salvage Tag info
width = 600
height = 350
date_nums = "".join((month, date, year))
barcode_text = "".join((division, store, date_nums))
file_name = "".join((barcode_text, ".png"))
print_string = "\n".join((div_string, store_string, date_string))
sticker_folder = "salvage_stickers"
sticker_path = os.path.join(os.getcwd(), sticker_folder, file_name)

if not os.path.exists(sticker_path):
    print(barcode_text)
    default_small = ImageFont.truetype("arial.ttf", 20)
    default_large = ImageFont.truetype("arial.ttf", 32)
    barcode_font = ImageFont.truetype("fonts/code128.ttf", 100)
    barcode_location = (width*.1, height*.1)
    barcode_text_line_location = (width*.35, height*.45)
    barcode_printstring_location = (50, height*.60)
    im = Image.new("RGB", (width, height), "white")
    sticker = ImageDraw.ImageDraw(im)

    sticker.text(barcode_location, barcode_text, font=barcode_font, fill="black")
    sticker.text(barcode_text_line_location, barcode_text, font=default_small, fill="black")
    sticker.text(barcode_printstring_location, print_string, font=default_large, fill="black")
    im.show()

def get_barcode_text(bct):
    pass

class SalvageSticker:

    def __init__(self):
        self.img = ""


def create_blank_page():
    size = (2550, 3300)
    im = Image.new("RGB", size, "white")
    background = ImageDraw.Draw(im)
    return [im, background]


def puzzler(bg_object, placeable, left_edge_buffer, placeablebuffer):
    #bj_object
    pass

page = create_blank_page()
# page[0].show()
print(print_string)



