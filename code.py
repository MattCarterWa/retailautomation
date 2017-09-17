from barcode import Barcode


class Code:
    def __init__(self, code):
        self.text = ""
        self.original = str(code)
        self.type = ""

    def barcode(self):
        return Barcode(self.text)

    def detect_type(self, info=False):
        print(self.original)
        if len(self.original) == 11:
            # I might be a shortened F4T
            # Just add Check Digit
            converting = self.original
            converting += self.calc_check_digit(self.upc)
            self.text = converting
            self.type = "F4T"
            if info:
                print(self.text, converting)
            return True
        elif len(self.original) == 12:
            # I might be just a upc.
            # so I should be valid.
            self.type = "UPC"
            return True
        elif len(self.original) == 13:
            converting = self.upc[-11:]
            check_d = self.calc_check_digit(converting)
            print(check_d)
            ###Added to handle 13digit upcs that should be leading with a 0.
            if check_d == "10":  # and converting[len(converting)-1] == "0":
                # converting = converting[:len(converting)-1]
                # print(converting)
                # converting += self.calc_check_digit(converting)
                # converting += "0"
                print(converting)
            #########
            self.upc = converting + check_d
            print(self.upc, converting)
            return True
        elif len(self.original) == 14:
            if self.upc[-1] == "0":
                converting = self.upc[-12:]
                converting = converting[:11]
                converting += self.calc_check_digit(converting)
                self.upc = converting
                print(self.upc)
                return True
            else:
                self.upc = self.upc[-12:]
            # converting = self.upc
            return True

            # I might be an F4T or A3T tag or a UPT
            # Drop the leading 2 00s and add the check digit.
            # Or grab the last 11 digits, then add the check digit.
        else:
            return False

if __name__ == "__main__":
    code = Code()
