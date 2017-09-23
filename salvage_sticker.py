from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from salvage_sticker_barcode import generate_barcode, get_binary
import os
from papers import create_blank_page

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
    # print(barcode_text)
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


def convert_to_binary(bct):
    i = 1
    start_binary = "11010011100"
    end_binary = "1100011101011"
    check_digit = 105
    odd = len(bct) % 2
    pairs = int(len(bct)/2)
    last_pair = 0
    binary = ""
    for pair in range(pairs):
        target = 2 + 2*pair
        combo = int(bct[last_pair: target])
        check_digit += combo * i
        last_pair = target
        i += 1
        # print(combo)
        binary += get_binary(str(combo))

    if odd == 1:
        last_num = int(bct[-1]) * i
        check_digit += last_num
        binary += get_binary(str(last_num))
        print(bct[-1])

    check_digit %= 103
    binary += get_binary(str(check_digit))
    binary = start_binary + binary + end_binary
    bct += str(check_digit)
    # print(binary)
    # print(bct)
    return binary



   # check_digit = check_digit % 103


  #  start_binary = "11010011100"
  #  end_binary = "1100011101011"


# page = create_blank_page()
# page[0].show()
# print(print_string)
# print(convert_to_binary(barcode_text))



