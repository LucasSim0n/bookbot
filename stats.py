def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1

    return chars


def get_report(chars):
    report = []
    for char in chars:
        if not char.isalpha():
            continue
        rep_char = {"char": char, "num": chars[char]}
        report.append(rep_char)

    return report


def sort_on(report):
    return report["num"]
