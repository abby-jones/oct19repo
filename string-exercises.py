# calculate the length of a string
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('abby'))

# frequency of letters in a string
def char_freq(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_freq('jones'))

def string_both_ends(str):
    if len(str) < 2
      return ''
    return str[0:2] + str[-2:]
print(string_both_ends('abbyjones'))
print(string_both_ends('ab'))
print(string_both_ends('a'))