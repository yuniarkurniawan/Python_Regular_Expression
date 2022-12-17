import re

tmp_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(tmp_string)


# for match in matches:
#     print(f'{match}')

# akan mencetak
# <re.Match object; span=(3, 6), match='abc'>
# <re.Match object; span=(12, 15), match='abc'>


# ============ span()
# for match in matches:
#     print(f'{match.span()}')
# akan mencetak
# (3, 6)
# (12, 15)


# ============ span(), start() dan end()
for match in matches:
    print(f'{match.span()} - {match.start()} - {match.end()}')
# akan mencetak
# (3, 6) - 3 - 6
# (12, 15) - 12 - 15
