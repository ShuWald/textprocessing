# So right off the bat in the assignment Part A requirements I noticed "List<Token>", "Map<Token,Count>", and more, all of which are implying that `Token` is a data type? The quickest, most minimal implementation is just using a class

class Token:
    # Class stores and outputs like a string
    def __init__(self, token: str):
        self.token = token

# Time Complexity: O(n)
def tokenize(filepath: str) -> list[Token]:
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    all_tokens: list[Token] = []

    # So obviously the first question is how to split the text into tokens efficiently, especially without the use of regex. 
    # The obvious function to use is the python split() method, which seperates strings on delimiters. However, you are only able to define one delimiter. Which means that we would have to repeat this for  possible delimiters that could be in the text, if we want to meet the requirements that tokens only consist of alphanumeric characters.
    # Another solution is implementing a splitting method yourself that checks on all possible delimiters for each character. However, the assignment, once again, only defines what a valid token character is: any alphanumeric values. So this method of checking all non-token characters would require knowing (in advance) and checking for all of them, which is inefficient
    # So a solution would require scanning the text itself for all possible nonvalid token characters and running split() for each one. 
    # While it can be somewhat optimized this is still O(n^2) time complexity which is horrible. 

    # However I realized an even better solution, since using python's isalphanum() method we can replace any non-alphanumeric value with a space " ", a run that will only take O(n) time complexity. 
    no_specials = ""
    for char in text:
        clean_char = char if char.isalnum() else " "
        no_specials += clean_char

    # Other steps are easily handled by built-in Python functions (Which are also O(n) time)
    all_tokens = no_specials.lower().split()

    # Overall O(n) time complexity
    return all_tokens


# Time Complexity: O(n)
# Dictionaries are the python equivalent of maps
def computeWordFrequencies(all_words: list[Token]) -> dict[Token, int]:
    word_counts: dict[Token, int] = {}

    # Using collections.Counter library would be most efficient, but I decided to implement it myself
    for word in all_words:
        if word in word_counts:
            word_counts[word] += 1
        else: 
            word_counts[word] = 1

    # Time complexity is O(n) since loop runs through all words in the list once
    return word_counts

# Time Complexity: O(n log n)
def printFrequencies(frequencies: dict[Token, int]) -> None:
    # Can use sorted() function to sort the dictionary by value, which is O(n log n) time complexity.
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: (x[1], x[0]) , reverse=True)

    # Print, O(n) time
    for word, freq in sorted_frequencies:
        print(f"{word} > {freq}")




import sys


def main():
    if len(sys.argv) < 2:
        print('Error: No file path provided.')
        sys.exit(1)

    print('Tokenizing file...')
    filepath = sys.argv[1]
    tokens = tokenize(filepath)
    frequencies = computeWordFrequencies(tokens)
    printFrequencies(frequencies)

if __name__ == '__main__':
  main()