def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':' character.
    
    Args:
        text (str): The text to be processed.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    result = ''
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue  # Skip spaces right after punctuation
        skip_space = False

        result += char
        if char in special_chars:
            result += '\n\n'
            skip_space = True

    # Print each non-empty line without leading/trailing spaces
    for line in result.split('\n'):
        line = line.strip()
        if line:
            print(line)
