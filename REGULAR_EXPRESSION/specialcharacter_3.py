import re

# spesial karakter '\s' digunakan untuk mencari 
# white space (space " ", tab "\t" newline "\n")
# pada tmp_string

tmp_string = 'hello 123_ heyho hohey \n'
pattern = re.compile(r'\s')
matches = pattern.finditer(tmp_string)

for match in matches:
    print(f'{match} :: {match.span()} :: {match.group()}')

# akan mencetak
# <re.Match object; span=(5, 6), match=' '> :: (5, 6) ::  
# <re.Match object; span=(10, 11), match=' '> :: (10, 11) ::  
# <re.Match object; span=(16, 17), match=' '> :: (16, 17) :: 
# <re.Match object; span=(23, 24), match='\n'> :: (23, 24) ::
