import sys

from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars_by_count


def get_book_text(path_to_file):
    file_text = ""
    with open(path_to_file) as f: 
        file_text = f.read()

    return file_text


def main(): 
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    book_file_path = sys.argv[1]
    print(f"Book to analyze: {book_file_path}")
    print("============ BOOKBOT ============")
    #book_file_path = "./books/frankenstein.txt"

    print(f"Analyzing book found at {book_file_path}") 
    book_text = get_book_text(book_file_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_num_chars(book_text)
    sorted_char_counts = sort_chars_by_count(char_counts)

    # Pretty-print the sorted list of char counts
    for char in sorted_char_counts:
        if char['char'].isalpha(): 
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()
