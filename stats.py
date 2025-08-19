def get_num_words(text):
    num_words = 0
    for word in text.split(): 
        num_words += 1
    return num_words


def get_num_chars(text): 
    char_counts = {}
    for word in text.split():
        for char in word.lower():
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
    return char_counts


# A function that takes a dictionary and returns the value of the "num" key 
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]


def sort_chars_by_count(char_counts): 
    sorted_char_counts = []
    # Create a list of dictionaries containing the char and the number of times 
    # it appeared in the text
    for char in char_counts:
        sorted_char_counts.append({'char': char, 'num': char_counts[char]})

    # Sort the list of dictionaries using the sort_on function above
    sorted_char_counts.sort(reverse=True, key=sort_on)

    return sorted_char_counts
