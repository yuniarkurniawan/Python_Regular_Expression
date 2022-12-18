import re


# spesial karakter '\w' digunakan untuk mencari 
# karakter SELAIN ALPHANUMERIC (word) [a-zA-Z0-9_]

tmp_string = 'hello 123_ (*&^%$#@#$%^,. hohey \n'
pattern = re.compile(r'\W')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')

# akan mencetak 
# <re.Match object; span=(5, 6), match=' '> :: (5, 6) ::  
# <re.Match object; span=(10, 11), match=' '> :: (10, 11) ::  
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
# <re.Match object; span=(25, 26), match=' '> :: (25, 26) ::  
# <re.Match object; span=(31, 32), match=' '> :: (31, 32) ::  
# <re.Match object; span=(32, 33), match='\n'> :: (32, 33) ::