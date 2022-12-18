import re

tmp_string = 'hello 123_ (*&^%$#@#$%^,.; hohey \n'
pattern = re.compile(r'\S')
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
# <re.Match object; span=(11, 12), match='('> :: (11, 12) :: (
# <re.Match object; span=(12, 13), match='*'> :: (12, 13) :: *
# <re.Match object; span=(13, 14), match='&'> :: (13, 14) :: &
# <re.Match object; span=(14, 15), match='^'> :: (14, 15) :: ^
# <re.Match object; span=(15, 16), match='%'> :: (15, 16) :: %
# <re.Match object; span=(16, 17), match='$'> :: (16, 17) :: $
# <re.Match object; span=(17, 18), match='#'> :: (17, 18) :: #
# <re.Match object; span=(18, 19), match='@'> :: (18, 19) :: @
# <re.Match object; span=(19, 20), match='#'> :: (19, 20) :: #
# <re.Match object; span=(20, 21), match='$'> :: (20, 21) :: $
# <re.Match object; span=(21, 22), match='%'> :: (21, 22) :: %
# <re.Match object; span=(22, 23), match='^'> :: (22, 23) :: ^
# <re.Match object; span=(23, 24), match=','> :: (23, 24) :: ,
# <re.Match object; span=(24, 25), match='.'> :: (24, 25) :: .
# <re.Match object; span=(25, 26), match=';'> :: (25, 26) :: ;
# <re.Match object; span=(27, 28), match='h'> :: (27, 28) :: h
# <re.Match object; span=(28, 29), match='o'> :: (28, 29) :: o
# <re.Match object; span=(29, 30), match='h'> :: (29, 30) :: h
# <re.Match object; span=(30, 31), match='e'> :: (30, 31) :: e
# <re.Match object; span=(31, 32), match='y'> :: (31, 32) :: y
