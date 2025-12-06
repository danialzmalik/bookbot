from collections import defaultdict


def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}")
    with open(filepath) as f:
        contents = f.read()
    return contents


def count_words(long_text: str):
    split = long_text.split()

    # count every word#
    x = 0
    for word in split:
        x += 1

    print(f"{'-'*12} Word Count {'-'*13}")
    print(f"Found {len(split)} total words")
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

    print(f"{'-'*10} Character Count {'-'*10}")
    return sorted_dict


def sorted_list_of_dicts(input_dict: dict):
    """
    create list of dicts sorted by num [(char: , num: )].
    input is dict.
    output will be list of dicts [(char: , num: )].
    """

    # step 1: splice into char and num dict
    # step 2: create list of dicts
    list_of_dicts = []
    for key in input_dict.keys():
        char_dict = {}

        char_dict["char"] = key
        char_dict["num"] = input_dict[key]
        list_of_dicts.append(char_dict)

    # step 3: sort list by values
    sorted_list = sorted(list_of_dicts, key=lambda d: d["num"], reverse=True)

    return sorted_list
