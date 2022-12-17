import re

tmp_string = '123abc456789abc1011ABC'

# r digunakan untuk menjadikan semuanya menjadi row string
# contoh
# tmp_tab = '\tAdatab'
# maka akan mencetak '  Adatab'
# tapi ketika menggunakan r'\tAdatab'
# maka akan mencetak '\tAdatab'
# disini \t akan diperlakukan sebagai string

pattern = re.compile(r'abc')

# fungsi finditer() digunakan untuk pencarian pada tmp_string
# dengan pattern tertentu dan return object re.Match sprti contoh dibawah
matches = pattern.finditer(tmp_string)

for data in matches:
    print(f'{data}')

# akan mencetak
# <re.Match object; span=(3, 6), match='abc'>
# <re.Match object; span=(12, 15), match='abc'>