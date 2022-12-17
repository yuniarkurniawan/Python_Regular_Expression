import re

# mirip dengan fungsi match(), fungssi search() akan mencari
# pattern string pada tmp_string tidak harus pada indeks pertama
# saja dan hanya akan mengembalikan satu kali saja

tmp_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')

matches = pattern.search(tmp_string)
print(f'{matches}')
# akan mencetak <re.Match object; span=(3, 6), match='abc'>
