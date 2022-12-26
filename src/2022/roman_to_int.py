conversion_lookup = {
    "IV": "IIII",
    "IX": "VIIII",
    "XL": "XXXX",
    "XC": "LXXXX",
    "CD": "CCCC",
    "CM": "DCCCC"
}
master_lookup = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Convert:
    @staticmethod
    def convert_rom_to_int(roman) -> int:
        assert roman is not ""
        for k, v in conversion_lookup.items():
            if k in roman:
                roman = roman.replace(k, v)

        value=sum([master_lookup[char] for char in roman])
        return value


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--input_roman', help="input roman letter", type=str)
args = parser.parse_args()
converter = Convert()

int_value = converter.convert_rom_to_int(args.input_roman)
print(int_value)
