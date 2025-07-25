from stats import count_words, frequency, get_sorted_frequency
import sys

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    word_counts = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")
    freq = get_sorted_frequency(frequency(text))
    for v in freq:
        print(f"{v['char']}: {v['count']}")
    print("============= END ===============")

main()
