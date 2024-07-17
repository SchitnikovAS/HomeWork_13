calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    n = (len(string), string.upper(), string.lower())
    return n


def is_contains(string, list_one):
    count_calls()
    n = string.lower() in (item.lower() for item in list_one)
    return n


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
