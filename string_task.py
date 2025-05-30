def string_length(s):
    return len(s)

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def first_last_2(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]

def replace_char(s):
    first_char = s[0]
    rest = s[1:].replace(first_char, '$')
    return first_char + rest

def swap_first_two(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]

def add_ing_ly(s):
    if len(s) < 3:
        return s
    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

def not_poor(s):
    not_pos = s.find('not')
    poor_pos = s.find('poor')
    if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
        return s[:not_pos] + 'good' + s[poor_pos+4:]
    return s

def list_and_tuple():
    s = input("Enter comma-separated numbers: ")
    lst = s.split(',')
    tpl = tuple(lst)
    print("List :", lst)
    print("Tuple :", tpl)


print(string_length("hello"))
print(char_frequency("google.com"))
print(first_last_2("spring"))
print(replace_char("restart"))
print(swap_first_two("abc", "xyz"))
print(add_ing_ly("abc"))
print(add_ing_ly("string"))
print(not_poor("The lyrics is not that poor!"))
print(not_poor("The lyrics is poor!"))
list_and_tuple()
