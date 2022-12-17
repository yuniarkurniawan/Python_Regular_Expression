import re

tmp_string = '123abc456789abc1011ABC'
pattern = re.compile(r'abc')

# fungsi findall() digunakan untuk pencarian pada tmp_string
# dengan pattern tertentu dan return berupa string yang dicari
matches = pattern.findall(tmp_string)

for data in matches:
    print(f'{data}')

# akan mencetak 
# abc
# abc
