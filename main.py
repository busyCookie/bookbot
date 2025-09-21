import sys
from stats import get_num_words
from stats import get_chars_stats
from stats import sort_stats

def main():
    book_path = ""

    try:
        book_path = sys.argv[1]
    except Exception as e:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    stats = get_chars_stats(text)
    sorted_stats = sort_stats(stats)

    print(f"{num_words} words found in the document")
    print_report(book_path, num_words, sorted_stats)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["entry"].isalpha():
            continue
        print(f"{item['entry']}: {item['num']}")

    print("============= END ===============")

main()
