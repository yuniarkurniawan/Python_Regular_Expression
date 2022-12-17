import re

# # meta karakter '\.' akan mencari karakter '.'
tmp_string = '1.23abc123ABC.'
pattern = re.compile(r'\.')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')
# akan mencetak
# <re.Match object; span=(1, 2), match='.'> :: (1, 2) :: .
# <re.Match object; span=(13, 14), match='.'> :: (13, 14) :: .