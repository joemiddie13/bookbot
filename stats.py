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

def sort_chars_dict(chars_dict):
    # Convert dictionary to list of dictionaries
    chars_list = [{"char": char, "count": count} for char, count in chars_dict.items()]
    
    # Sort the list by count in descending order
    chars_list.sort(key=lambda item: item["count"], reverse=True)
    
    return chars_list