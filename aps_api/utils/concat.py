import random


def concat_variable(concatenados):
    random_numbers = ''.join(str(num) for num in random.sample(range(100, 1000), 3))
    concat = ''
    for i in concatenados:
        concat += i
    concat + random_numbers
    return concat


def concat_variable_special(concatenados):
    concat = ''
    for i in concatenados:
        concat += i
    return concat
