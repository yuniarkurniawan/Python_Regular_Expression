import re

# spesial karakter '\d' digunakan untuk mencari karakter DIGIT
# pada semua tmp_string 

tmp_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\d')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} - {match.group()}')

# akan mencetak
# <re.Match object; span=(6, 7), match='1'> :: (6, 7) - 1
# <re.Match object; span=(7, 8), match='2'> :: (7, 8) - 2
# <re.Match object; span=(8, 9), match='3'> :: (8, 9) - 3
