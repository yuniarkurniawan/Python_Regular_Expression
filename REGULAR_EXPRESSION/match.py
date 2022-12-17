import re

# fungsi match() digunakan untuk mencari string 
# dari indeks PERTAMA pada string

tmp_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')

matches = pattern.match(tmp_string)
print(f'{matches}')
# akan mencetak None

pattern = re.compile(r'123')
matches = pattern.match(tmp_string)
print(f'{matches}')
# akan mencetak <re.Match object; span=(0, 3), match='123'>
# tampak bahwa pada 123 akhir sebelum ABC tidak akan tercetak
# karena fungsi match() dimulai pada indeks pertama
