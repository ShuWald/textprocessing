import sys
from PartA import tokenize, computeWordFrequencies

# Time Complexity: O(n log n)
def commonTokens(freqs1: dict, freqs2: dict) -> int:
    # Find common tokens through intersection command, O(n) time complexity
    common = set(freqs1.keys()) & set(freqs2.keys())

    # Unsorted printing, O(n) time. Assignment only asked to optionally print common tokens.
    for word in common:
        print(f"{word} - File 1: {freqs1[word]}, File 2: {freqs2[word]}")
        
    return len(common)

def main():
    if len(sys.argv) < 3:
        print('Error: Two file paths required.')
        sys.exit(1)

    common_count = commonTokens(
        computeWordFrequencies(tokenize(sys.argv[1])), 
        computeWordFrequencies(tokenize(sys.argv[2]))
    )
    
    print(f"\nTotal common tokens: {common_count}")

if __name__ == '__main__':
    main()