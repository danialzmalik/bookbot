from stats import count_words, get_book_text, char_count

FRAKEN_PATH = "books/frankenstein.txt"


def main():
    frakenstein_txt = get_book_text(FRAKEN_PATH)
    char_dict = char_count(frakenstein_txt)


if __name__ == "__main__":
    main()
