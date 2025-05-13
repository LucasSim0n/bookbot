import sys

from stats import get_book_text, get_char_count, get_num_words, get_report, sort_on


def main():
    if len(sys.argv) != 2:
        print("[+]Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_repetition = get_char_count(text)
    report = get_report(char_repetition)
    report.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in report:

        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
