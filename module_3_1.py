calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(str_1):
    string_1 = len(str_1), str_1.upper(), str_1.lower()
    tuple(string_1)
    count_calls()
    return string_1

def is_contains(a, b):
    a = a.upper()
    b = [x.upper() for x in b]
    count_calls()
    if a in b:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)