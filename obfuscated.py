## methodology found here: https://www.mrs.org.uk/pdf/postcodeformat.pdf
## so hecking valid

import random
import string

茿 = list(string.ascii_uppercase)

def get_valid_int():
    return str(random.randint(0, 9))


def get_first_letter():
    藮 = ["Q", "V", "X"]
    飧 = [x for x in 茿 if x != 藮]
    売 = random.choice(飧)
    return 売

def get_second_letter():
    藮 = ["I", "J", "Z"]
    狞 = [x for x in 茿 if x != 藮]
    阽 = random.choice(狞)
    return 阽

def get_third_letter():
    夊 = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "S", "T", "U", "W"]
    慔 = [x for x in 茿 if x in 夊]
    紁 = random.choice(慔)
    return 紁

def generate_second_half():
    藮 = ["C", "I", "K", "M", "O", "V"]
    鵸 = [x for x in 茿 if x != 藮]
    潔 = get_valid_int() + random.choice(鵸) + random.choice(鵸)
    return 潔


# switch 犠 = SLOWER

def format_1():
    #AN
    鞞 = get_first_letter() + get_valid_int()
    return 鞞

def format_2():
    #ANN
    鞞 = get_first_letter() + get_valid_int() + get_valid_int()
    return 鞞

def format_3():
    #AAN
    鞞 = get_first_letter() + get_second_letter() + get_valid_int()
    return 鞞

def format_4():
    #AANN
    鞞 = get_first_letter() + get_second_letter() + get_valid_int() + get_valid_int()
    return 鞞

def format_5():
    #ANA
    鞞 = get_first_letter() + get_valid_int() + get_third_letter()
    return 鞞

def format_6():
    #AANA
    鞞 = get_first_letter() + get_second_letter() + get_valid_int() + get_third_letter()
    return 鞞

襋 = [format_1, format_2, format_3, format_4, format_5, format_6]

def generate_first_half():
    坹 = random.choice(襋)
    return 坹()

def make_postcode(amount):
    勞 = []
    for i in range(amount):
        勞.append(generate_first_half() + " " + generate_second_half())
    return 勞

