import re

# spesial karakter '\w' digunakan untuk mencari 
# karakter ALPHANUMERIC (word) [a-zA-Z0-9_]

tmp_string = 'hello 123_ (*&^%$#@#$%^,, hohey \n'
pattern = re.compile(r'\w')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')

# akan mencetak
# <re.Match object; span=(0, 1), match='h'> :: (0, 1) :: h
# <re.Match object; span=(1, 2), match='e'> :: (1, 2) :: e
# <re.Match object; span=(2, 3), match='l'> :: (2, 3) :: l
# <re.Match object; span=(3, 4), match='l'> :: (3, 4) :: l
# <re.Match object; span=(4, 5), match='o'> :: (4, 5) :: o
# <re.Match object; span=(6, 7), match='1'> :: (6, 7) :: 1
# <re.Match object; span=(7, 8), match='2'> :: (7, 8) :: 2
# <re.Match object; span=(8, 9), match='3'> :: (8, 9) :: 3
# <re.Match object; span=(9, 10), match='_'> :: (9, 10) :: _
# <re.Match object; span=(24, 25), match='h'> :: (24, 25) :: h
# <re.Match object; span=(25, 26), match='o'> :: (25, 26) :: o
# <re.Match object; span=(26, 27), match='h'> :: (26, 27) :: h
# <re.Match object; span=(27, 28), match='e'> :: (27, 28) :: e
# <re.Match object; span=(28, 29), match='y'> :: (28, 29) :: y