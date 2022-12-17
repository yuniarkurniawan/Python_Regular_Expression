import re

# meta karakter '.' akan mencari semua karakter kecuali \n

tmp_string = '123abc123ABC'
pattern = re.compile(r'.')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')

# akan mencetak
# <re.Match object; span=(0, 1), match='1'> :: (0, 1) :: 1
# <re.Match object; span=(1, 2), match='2'> :: (1, 2) :: 2
# <re.Match object; span=(2, 3), match='3'> :: (2, 3) :: 3
# <re.Match object; span=(3, 4), match='a'> :: (3, 4) :: a
# <re.Match object; span=(4, 5), match='b'> :: (4, 5) :: b
# <re.Match object; span=(5, 6), match='c'> :: (5, 6) :: c
# <re.Match object; span=(6, 7), match='1'> :: (6, 7) :: 1
# <re.Match object; span=(7, 8), match='2'> :: (7, 8) :: 2
# <re.Match object; span=(8, 9), match='3'> :: (8, 9) :: 3
# <re.Match object; span=(9, 10), match='A'> :: (9, 10) :: A
# <re.Match object; span=(10, 11), match='B'> :: (10, 11) :: B
# <re.Match object; span=(11, 12), match='C'> :: (11, 12) :: C