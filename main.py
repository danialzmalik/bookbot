from stats import count_words, get_book_text, char_count, sorted_list_of_dicts

FRAKEN_PATH = "books/frankenstein.txt"


def main():
    print(f"{"="*10} BOOKBOT {"="*10}")

    frakenstein_txt = get_book_text(FRAKEN_PATH)

    word_count = count_words(frakenstein_txt)
    char_dict = char_count(frakenstein_txt)

    sorted_list = sorted_list_of_dicts(char_dict)
    for dict in sorted_list:
        c = dict["char"]
        if c.isalpha():
            print(f"{c}: {dict["num"]}")


if __name__ == "__main__":
    main()
