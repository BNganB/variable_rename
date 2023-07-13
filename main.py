import obfuscate_me as tf
import re
import translate_vari as tv

unclean_variables = dir(tf)
remove_me = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'global_vars', 'local_vars']

with open("obfuscate_1.py", "r") as f:
    old_file_raw = f.read()

new_file_raw = old_file_raw

# exclude imports, will break program
pattern = r'(?<!import)\s+(\w+)\s*='

# get valid renaming targets
only_variables = [match for match in re.findall(pattern, new_file_raw) if match not in remove_me]

def get_only_translated_variables(only_variables):
    only_translated_variables = []
    for variable in only_variables:
        only_translated_variables.append(tv.translate_given_variable(variable))

    return only_translated_variables


for i in range(len(only_variables)):
    new_file_raw = re.sub(r'\b{}\b'.format(only_variables[i]), get_only_translated_variables(only_variables)[i], new_file_raw) #CHANGE gen_x to change language

with open("obfuscated.py", "w") as f:
    f.write(new_file_raw)
