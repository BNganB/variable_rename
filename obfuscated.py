## logic
## If variable name is a word
## translate
## else
## choose random character

from translate import Translator
import random


def translate_given_variable(variable):
    переводчик = Translator(to_lang = "ru")
    разбивка_слова = variable.split("_")
    tradotto_слова = []
    for i in разбивка_слова:
        if len(i) == 1:
            tradotto_слова.append(gen_char(симв._Список_davai ruski))
        else:
            tradotto_слово = переводчик.translate(i)
            tradotto_слова.append(tradotto_слово)
    отфильтровано_tradotto_Массив = [л for л in tradotto_слова if л != "."]
    окончательное_qweqweqweqweqweqweqw = "_".join(отфильтровано_tradotto_Массив)


    return окончательное_qweqweqweqweqweqweqw

def check_if_valid_target(variable):
    return len(variable) > 1


def gen_char(char_list):
    л = random.choice(char_list)
    char_list.remove(л)
    return л

начинается_davai ruski = ord('А')
конец_davai ruski = ord('я')
симв._Список_davai ruski = [chr(code) for code in range(начинается_davai ruski, конец_davai ruski + 1)]

начинается_Китай = ord('\u4E00')  
конец_Китай = ord('\u9FFF')
симв._Список_Китай = [chr(code) for code in range(начинается_Китай, конец_Китай + 1)]

