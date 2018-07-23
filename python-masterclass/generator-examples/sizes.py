import sys


def my_range(n: int):
    print('my_range starts')
    start = 0
    while start < n:
        print(f'my_range is returning {start}')
        yield start
        start += 1


_ = input('line 12')
# big_range = range(5)
big_range = my_range(5)
_ = input('line 15'
          '')
print(f'big_range is {sys.getsizeof(big_range)} bytes')

# create a list containing all the values in big_range
big_list = []

_ = input('line 22')
for val in big_range:
    _ = input('line 24 - inside loop')
    big_list.append(val)

print(f'big_list is {sys.getsizeof(big_list)} bytes')

print(big_range)
print(big_list)
