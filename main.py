from stats import count_words, get_book_text, char_count, sorted_list_of_dicts
import sys


def main():
    print(f"{"="*10} BOOKBOT {"="*10}")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    frakenstein_txt = get_book_text(sys.argv[1])

    word_count = count_words(frakenstein_txt)
    char_dict = char_count(frakenstein_txt)

    sorted_list = sorted_list_of_dicts(char_dict)
    for dict in sorted_list:
        c = dict["char"]
        if c.isalpha():
            print(f"{c}: {dict["num"]}")


if __name__ == "__main__":
    main()
