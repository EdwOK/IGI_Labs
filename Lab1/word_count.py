import re


def word_count(string):
    word_list = re.findall(r'[a-zA-Z]+', string)
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def top_ten_words(string):
    word_dict = word_count(string)
    return ' '.join(sorted(word_dict, key=word_dict.get, reverse=True)[:10]) + '.'
