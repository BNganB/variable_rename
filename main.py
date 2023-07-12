import obfuscate_me as tf
import re
import random

def gen_ruski(char_list):
    x = random.choice(char_list)
    char_list.remove(x)
    return x

def gen_china(char_list):
    x = random.choice(char_list)
    char_list.remove(x)
    return x

start_ruski = ord('А')
end_ruski = ord('я')
char_list_ruski = [chr(code) for code in range(start_ruski, end_ruski + 1)]

start_china = ord('\u4E00')  
end_china = ord('\u9FFF')
char_list_china = [chr(code) for code in range(start_china, end_china + 1)]

unclean_variables = dir(tf)
remove_me = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'global_vars', 'local_vars']

with open("obfuscate_me.py", "r") as f:
    content = f.read()

new_file_raw = content

# exclude imports, will break program
pattern = r'(?<!import)\s+(\w+)\s*='

# get valid renaming targets
only_variables = [match for match in re.findall(pattern, new_file_raw) if match not in remove_me]

for i in range(len(only_variables)):
    new_file_raw = re.sub(r'\b{}\b'.format(only_variables[i]), gen_china(char_list_china), new_file_raw) #CHANGE gen_x to change language

with open("obfuscated.py", "w") as f:
    f.write(new_file_raw)
