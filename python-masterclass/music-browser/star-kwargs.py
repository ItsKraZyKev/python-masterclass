def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)  # print first word seperatly
    # print (end=end_character)


with open('backwards.txt', 'w') as backwards:
    print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='\n')
    print('Another string')

print()
print('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='', sep='\n**\n')
print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='', sep='\n**\n')
print('=' * 10)
