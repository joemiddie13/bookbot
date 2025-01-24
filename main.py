def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_chars_dict(text)
    print_report(book_path, num_words, char_counts)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():  # Only count alphabetic characters
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, word_count, char_counts):
    # Print the header
    print(f"--- Here's the report for {book_path} ---")
    print(f"Total words found: {word_count}\n")
    
    # Convert char_counts to a list of tuples and sort
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Print each character and its count
    for char, count in sorted_chars:
        print(f"The character '{char}' appeared {count} times.")
    
    # Print the footer
    print("--- End of report ---")

# Call the main function
if __name__ == "__main__":
    main()