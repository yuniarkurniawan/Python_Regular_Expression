import re

# meta karakter '$' digunakan untuk pencarian pada tmp_string
# yang DIAKHIRI dengan karakter pattern

tmp_string = '123abc123ABC'
pattern = re.compile(r'ABC$')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')
# akan mencetak <re.Match object; span=(9, 12), match='ABC'> :: (9, 12) :: ABC

pattern_2 = re.compile(r'abc$')
matches_2 = pattern_2.finditer(tmp_string)

for match in matches_2:
    print(f'{match} :: {match.span()} :: {match.group()}')
# TIDAK AKAN MENCETAK APAPUN
