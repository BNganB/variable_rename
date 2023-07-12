>input = obfuscate_me.py
>output = obfuscated.py


Change line 38 for language select
```
new_file_raw = re.sub(r'\b{}\b'.format(only_variables[i]), #CHANGEME#, new_file_raw)
```
