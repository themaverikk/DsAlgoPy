import string
from collections import OrderedDict


def remove_vowels(string_with_vowels):
    if not string_with_vowels:
        return string_with_vowels
    vowels = ('a', 'e', 'i', 'o', 'u')

    return ''.join([l for l in string_with_vowels if l not in vowels])


def remove_duplicates(string_with_duplicates):
    return "".join(OrderedDict.fromkeys(string_with_duplicates))


def encode_string(s):
    without_vowels = remove_vowels(s)
    without_dups = remove_duplicates(without_vowels)
    with_start_appended = without_dups + without_dups[0]

    alphabet_index = {}
    reverse_alphabet_index = {}

    for char in string.ascii_lowercase:
        index = ord(char) - ord('a') + 1

        alphabet_index[char] = index
        reverse_alphabet_index[index] = char

    encoded_str = ''
    for i in range(len(with_start_appended) - 1):
        next_char_index = alphabet_index[with_start_appended[i]] + alphabet_index[with_start_appended[i + 1]]
        next_char_index = (next_char_index % 27) + 1 if next_char_index > 26 else next_char_index
        next_char = reverse_alphabet_index[next_char_index]
        encoded_str += next_char

    return encoded_str


encode_string('yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxioioioioio')
