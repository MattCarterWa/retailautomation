from PIL import Image, ImageDraw

# Creates the background the stickers will print on
def create_blank_page():
    size = (2550, 3300)
    im = Image.new("RGB", size, "white")

    background = ImageDraw.Draw(im)
    return [im, background]


class BarcodePage:
    def __init__(self):
        self.page, self.background = create_blank_page()
        self.x1 = -1
        self.y1 = -1
        self.x2 = 0
        self.y2 = 0
        self.pages = []
        self.current_row = 0
        self.current_column = 0
        self.max_row = None
        self.max_column = None

    @property
    def location(self):
        box = (self.x1, self.y1, self.x2, self.y2)
        return box

    def add_sticker(self, barcode):
        if not self.max_row:
            self.max_row = self.page.size[0] / barcode.barcode_width
            self.max_column = self.page.size[1] / barcode.barcode_height

        if self.current_row < self.max_row:
            if self.current_column < self.max_column:
                self.x1, self.y1 = self.x2, self.y2
                self.x2 = barcode.barcode_width + barcode.barcode_width * self.current_column
                self.y2 += barcode.barcode_height + barcode.barcode_height * self.current_row
                self.page.paste(barcode.image, self.location)
                self.current_column += 1
            self.current_row += 1



