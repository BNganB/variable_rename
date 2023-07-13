## logic
## If variable name is a word
## translate
## else
## choose random character

from translate import Translator
import random


def translate_given_variable(variable):
    translator = Translator(to_lang = "ru")
    split_words = variable.split("_")
    translated_words = []
    for i in split_words:
        if len(i) == 1:
            translated_words.append(gen_char(char_list_ruski))
        else:
            translated_word = translator.translate(i)
            translated_words.append(translated_word)
    filtered_translated_array = [x for x in translated_words if x != "."]
    final_str = "_".join(filtered_translated_array)


    return final_str

def check_if_valid_target(variable):
    return len(variable) > 1


def gen_char(char_list):
    x = random.choice(char_list)
    char_list.remove(x)
    return x

start_ruski = ord('А')
end_ruski = ord('я')
char_list_ruski = [chr(code) for code in range(start_ruski, end_ruski + 1)]

start_china = ord('\u4E00')  
end_china = ord('\u9FFF')
char_list_china = [chr(code) for code in range(start_china, end_china + 1)]

