from itertools import permutations

def word_to_number(word, assignment):
    return int(''.join(str(assignment[char]) for char in word))

def solve_cryptarithmetic(word1, word2, result_word):
    # Get all unique letters
    unique_letters = set(word1 + word2 + result_word)

    if len(unique_letters) > 10:
        print("Too many unique letters (max 10 allowed in base-10 digits).")
        return

    letters = list(unique_letters)
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        assignment = dict(zip(letters, perm))

        # Check for leading zeros
        if assignment[word1[0]] == 0 or assignment[word2[0]] == 0 or assignment[result_word[0]] == 0:
            continue

        # Convert words to numbers
        num1 = word_to_number(word1, assignment)
        num2 = word_to_number(word2, assignment)
        result = word_to_number(result_word, assignment)

        if num1 + num2 == result:
            print("Solution:")
            print(assignment)
            print(f"{word1} ({num1}) + {word2} ({num2}) = {result_word} ({result})")
            return

    print("No solution found.")

# Example usage
if __name__ == "__main__":
    word1 = input("Enter the first word: ").strip().upper()
    word2 = input("Enter the second word: ").strip().upper()
    result_word = input("Enter the result word: ").strip().upper()
    solve_cryptarithmetic(word1, word2, result_word)
