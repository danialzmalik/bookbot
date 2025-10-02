FRAKEN_PATH = "books/frankenstein.txt"


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


def main():
    frakenstein_txt = get_book_text(FRAKEN_PATH)
    # print(frakenstein_txt)
    count = count_words(frakenstein_txt)
    print(f"Found {count} total words")


if __name__ == "__main__":
    main()
