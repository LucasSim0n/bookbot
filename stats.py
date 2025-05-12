def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_words(text):
    return len(text.split())
