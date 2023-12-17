def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print_report(num_letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letters(text):
    text = text.lower()
    nums = {}
    for i in  text:
        if i in nums:
           nums[i] += 1
        else:
            nums[i] = 1
    return nums

def print_report(text):
    letters = list(text.keys())
    letters.sort()
    for l in letters:
        if l.isalpha():
            print(f"The '{l}' character was found {text[l]} times")
    print('--- End report ---')

main()