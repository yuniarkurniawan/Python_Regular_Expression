import re

# special karakter '\D' akan mencari karakter NON DIGIT pada 
# semua karakter tmp_string

tmp_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\D')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} - {match.group()}')

# akan mencetak sperti dibawah ini. Tampak bahwa karakter DIGIT tidak akan tercetak
# <re.Match object; span=(0, 1), match='h'> :: (0, 1) - h
# <re.Match object; span=(1, 2), match='e'> :: (1, 2) - e
# <re.Match object; span=(2, 3), match='l'> :: (2, 3) - l
# <re.Match object; span=(3, 4), match='l'> :: (3, 4) - l
# <re.Match object; span=(4, 5), match='o'> :: (4, 5) - o
# <re.Match object; span=(5, 6), match=' '> :: (5, 6) -  
# <re.Match object; span=(9, 10), match='_'> :: (9, 10) - _
# <re.Match object; span=(10, 11), match=' '> :: (10, 11) -  
# <re.Match object; span=(11, 12), match='h'> :: (11, 12) - h
# <re.Match object; span=(12, 13), match='e'> :: (12, 13) - e
# <re.Match object; span=(13, 14), match='y'> :: (13, 14) - y
# <re.Match object; span=(14, 15), match='h'> :: (14, 15) - h
# <re.Match object; span=(15, 16), match='o'> :: (15, 16) - o
# <re.Match object; span=(16, 17), match=' '> :: (16, 17) -  
# <re.Match object; span=(17, 18), match='h'> :: (17, 18) - h
# <re.Match object; span=(18, 19), match='o'> :: (18, 19) - o
# <re.Match object; span=(19, 20), match='h'> :: (19, 20) - h
# <re.Match object; span=(20, 21), match='e'> :: (20, 21) - e
# <re.Match object; span=(21, 22), match='y'> :: (21, 22) - y
