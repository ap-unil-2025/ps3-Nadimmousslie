"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = (
        "Python is a powerful programming language.\n"
        "It is widely used in web development, data science, and automation.\n"
        "Python's simple syntax makes it great for beginners.\n"
        "Many companies use Python for their projects."
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    return len(words)


def count_lines(filename):
    """
    Count total lines in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return len(lines)


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    if not include_spaces:
        text = text.replace(" ", "").replace("\n", "")
    return len(text)


def find_longest_word(filename):
    """
    Find and return the longest word in the file.
    """
    import string

    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()

    # Remove punctuation from words
    cleaned = [w.strip(string.punctuation) for w in words if w.strip(string.punctuation)]
    if not cleaned:
        return None
    return max(cleaned, key=len)


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    """
    import string
    frequency = {}

    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().lower().split()

    for w in words:
        w = w.strip(string.punctuation)
        if w:
            frequency[w] = frequency.get(w, 0) + 1

    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Charac
