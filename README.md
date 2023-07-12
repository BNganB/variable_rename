>input = obfuscate_me.py

>output = obfuscated.py


Change line 38 for language select
```
new_file_raw = re.sub(r'\b{}\b'.format(only_variables[i]), gen_char(CHAR_LIST_x), new_file_raw)
```
