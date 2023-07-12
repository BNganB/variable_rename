## methodology found here: https://www.mrs.org.uk/pdf/postcodeformat.pdf
## so hecking valid

import random
import string

letters = list(string.ascii_uppercase)

def get_valid_int():
    return str(random.randint(0, 9))


def get_first_letter():
    remove_me = ["Q", "V", "X"]
    first_pos_letters = [x for x in letters if x != remove_me]
    first_letter = random.choice(first_pos_letters)
    return first_letter

def get_second_letter():
    remove_me = ["I", "J", "Z"]
    second_pos_letters = [x for x in letters if x != remove_me]
    second_letter = random.choice(second_pos_letters)
    return second_letter

def get_third_letter():
    dont_remove_me = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "S", "T", "U", "W"]
    third_pos_letters = [x for x in letters if x in dont_remove_me]
    third_letter = random.choice(third_pos_letters)
    return third_letter

def generate_second_half():
    remove_me = ["C", "I", "K", "M", "O", "V"]
    second_half_letters = [x for x in letters if x != remove_me]
    second_half = get_valid_int() + random.choice(second_half_letters) + random.choice(second_half_letters)
    return second_half


# switch case = SLOWER

def format_1():
    #AN
    complete = get_first_letter() + get_valid_int()
    return complete

def format_2():
    #ANN
    complete = get_first_letter() + get_valid_int() + get_valid_int()
    return complete

def format_3():
    #AAN
    complete = get_first_letter() + get_second_letter() + get_valid_int()
    return complete

def format_4():
    #AANN
    complete = get_first_letter() + get_second_letter() + get_valid_int() + get_valid_int()
    return complete

def format_5():
    #ANA
    complete = get_first_letter() + get_valid_int() + get_third_letter()
    return complete

def format_6():
    #AANA
    complete = get_first_letter() + get_second_letter() + get_valid_int() + get_third_letter()
    return complete

first_half_format_list = [format_1, format_2, format_3, format_4, format_5, format_6]

def generate_first_half():
    choose_function = random.choice(first_half_format_list)
    return choose_function()

def make_postcode(amount):
    postcodes = []
    for i in range(amount):
        postcodes.append(generate_first_half() + " " + generate_second_half())
    return postcodes

