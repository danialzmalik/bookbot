from collections import defaultdict


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def count_words(long_text: str):
    split = long_text.split()

    # count every word#
    x = 0
    for word in split:
        x += 1

    return len(split)


def char_count(text_str):
    """
    create dict for chars
    loop text_str and add depending on char
    """
    char_dict = defaultdict(int)
    text_str = text_str.lower()
    for char in text_str:
        char_dict[char] += 1

    sorted_dict = dict(sorted(char_dict.items()))

    # for char in sorted_dict.items():
    #     print(f"'{char[0]}': {char[1]}")

    return sorted_dict
