def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    output(count_chars(book),count_words(book))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)


def count_chars(book):
    chars = {}
    lower_chars = book.lower()
    for char in lower_chars:
        if char not in chars and char.isalpha():
            chars[char] = 1
        elif char.isalpha():
            chars[char] += 1
    

    return chars


def sort_dict(item):
    return item["count"]

def sort_list(chars):
    chars_list = [{"name": char, "count": count} for char, count in chars.items()]
    chars_list.sort(reverse=True, key=sort_dict)
    return chars_list

def output(chars, words_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    sorted_list = sort_list(chars)
    for dict in sorted_list:
        print(f"The '{dict["name"]}' character was found {dict["count"]} times.")




main()