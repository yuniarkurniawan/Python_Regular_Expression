import re

# penggunaan meta karakter '^' digunakan untuk melakukan pencarian
# pada tmp_string dimulai dari indeks pertama  

tmp_string = '123abc123ABC'
pattern = re.compile(r'^123')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')

# akan mencetak
# <re.Match object; span=(0, 3), match='123'> :: (0, 3) :: 123



pattern_2 = re.compile('^abc')
matches_2 = pattern_2.finditer(tmp_string)

for match_2 in matches_2:
    print(f'{match_2}')

# TIDAK AKAN MENCETAK APAPUN
# tampak bahwa tmp_string tidak diawali dengan karakter 'abc'
