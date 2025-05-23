def first_non_repeating_char(s: str) -> str:
    """
    Returns the first non-repeating character in a given string.
    
    Parameters:
        s (str): The input string to search.
    
    Returns:
        str: The first non-repeating character, or an empty string if none exists.
    """
    from collections import OrderedDict  # Import OrderedDict to keep characters in order of appearance

    # Initialize an ordered dictionary to store character counts
    char_count = OrderedDict()

    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the dictionary to find the first character with a count of 1
    for char, count in char_count.items():
        if count == 1:
            return char  # Return the first non-repeating character

    return ''  # If all characters repeat, return an empty string


# Main block to test the function
if __name__ == "__main__":
    test_string = "aabbcddeffg"  # Define a test string
    result = first_non_repeating_char(test_string)  # Call the function with the test string
    print(f"The first non-repeating character is: '{result}'")  # Output the result

    # Expected output:
    # The first non-repeating character is: 'c'

