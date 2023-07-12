## methodology found here: https://www.mrs.org.uk/pdf/postcodeformat.pdf
## so hecking valid

import random
import string

蔿 = list(string.ascii_uppercase)

def get_valid_int():
    return str(random.randint(0, 9))


def get_first_letter():
    煫 = ["Q", "V", "X"]
    趿 = [x for x in 蔿 if x != 煫]
    鶥 = random.choice(趿)
    return 鶥

def get_second_letter():
    煫 = ["I", "J", "Z"]
    柚 = [x for x in 蔿 if x != 煫]
    鵧 = random.choice(柚)
    return 鵧

def get_third_letter():
    粡 = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "S", "T", "U", "W"]
    肇 = [x for x in 蔿 if x in 粡]
    瘁 = random.choice(肇)
    return 瘁

def generate_second_half():
    煫 = ["C", "I", "K", "M", "O", "V"]
    鍎 = [x for x in 蔿 if x != 煫]
    摚 = get_valid_int() + random.choice(鍎) + random.choice(鍎)
    return 摚


# switch 溗 = SLOWER

def format_1():
    #AN
    涙 = get_first_letter() + get_valid_int()
    return 涙

def format_2():
    #ANN
    涙 = get_first_letter() + get_valid_int() + get_valid_int()
    return 涙

def format_3():
    #AAN
    涙 = get_first_letter() + get_second_letter() + get_valid_int()
    return 涙

def format_4():
    #AANN
    涙 = get_first_letter() + get_second_letter() + get_valid_int() + get_valid_int()
    return 涙

def format_5():
    #ANA
    涙 = get_first_letter() + get_valid_int() + get_third_letter()
    return 涙

def format_6():
    #AANA
    涙 = get_first_letter() + get_second_letter() + get_valid_int() + get_third_letter()
    return 涙

孊 = [format_1, format_2, format_3, format_4, format_5, format_6]

def generate_first_half():
    淓 = random.choice(孊)
    return 淓()

def make_postcode(amount):
    摼 = []
    for i in range(amount):
        摼.append(generate_first_half() + " " + generate_second_half())
    return 摼

