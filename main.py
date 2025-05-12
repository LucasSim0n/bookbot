import stats


def main():
    text = stats.get_book_text("books/frankenstein.txt")
    num_words = stats.get_book_words(text)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
