import sys
from stats import get_num_words, get_chars_dict, sort_chars_dict

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line arguments
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_chars_dict(text)
    sorted_chars = sort_chars_dict(char_counts)
    print_report(book_path, num_words, sorted_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, word_count, char_counts):
    # Print the header
    print(f"--- Here's the report for {book_path} ---")
    print(f"Found {word_count} total words\n")
    
    # Print each character and its count
    for char_dict in char_counts:
        print(f"{char_dict['char']}: {char_dict['count']}")
    
    # Print the footer
    print("--- End of report ---")

# Call the main function
if __name__ == "__main__":
    main()