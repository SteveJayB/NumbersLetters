#################################################################
#                                                               #
#                     Stephen Bridgett                          #                                                 
#                Numbers and Letters Analyzed                   #
#                                                               #                                                
#################################################################

from collections import Counter
import time
import os

# Benchmark function to measure execution time of a function
def timeFunction(f, *args):
    start_time = time.time()  # Start timer
    result = f(*args)  # Execute function with arguments
    end_time = time.time()  # End timer
    total_time = end_time - start_time  # Calculate execution time
    return result, total_time

# Optimized sum of first n integers using formula
def one(n):
    """
    Computes the sum of the first n natural numbers using the formula: sum = n * (n + 1) / 2.
    """
    total = (n * (n + 1)) // 2  # Sum formula for first n natural numbers
    return f"The sum of {n}'s integers is {total}."

print("\n----------TEST ONE-----------")
for num in [23, 505, 10**7]:
    result, duration = timeFunction(one, num)
    print(result, f"Time taken: {duration:.6f} seconds\n")

# Get the directory where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))  
file_path = os.path.join(script_dir, "words.txt")  

# Function to check if a word exists in a dictionary file
def two(word):
    """
    Checks if a given word exists in the words.txt dictionary file.
    """
    try:
        with open(file_path, "r") as fobj:
            words = set(fobj.read().split())  # Load words into a set for fast lookup
        return f"True, '{word}' is a valid word!" if word in words else f"Uh oh, '{word}' is not a valid word. Try again."
    except FileNotFoundError:
        return "Error: words.txt file not found!"

print("----------TEST TWO-----------")
for word in ["run", "classroom", "kenfkqwnfck"]:
    result, duration = timeFunction(two, word)
    print(result, f"Time taken: {duration:.6f} seconds\n")

# Function to check if a word can be formed from given letters
def three(word, letters):
    """
    Checks if the given word can be formed using the letters available.
    Uses Counter to compare letter frequencies.
    """
    return f"Yes, '{word}' can be made from the letters '{letters}'!" if not Counter(word) - Counter(letters) \
           else f"Oops, it doesn't seem like '{word}' can be made from the letters '{letters}'. Try again."

print("---------TEST THREE----------")
test_cases = [("frog", "froglkdmveowwmwwefgm"), ("classroom", "jndfwdnw"), ("run", "rakfuvn")]
for word, letters in test_cases:
    result, duration = timeFunction(three, word, letters)
    print(result, f"Time taken: {duration:.6f} seconds\n")

# Helper function to load words from a dictionary file
def lookUp():
    """
    Reads words.txt and returns a set of words.
    """
    try:
        with open(file_path, "r") as f:
            return set(f.read().split())  # Read file into a set
    except FileNotFoundError:
        print(f"Error: words.txt file not found at {file_path}")
        return set()  # Return empty set to avoid crashing

wordMaster = lookUp()  # Load words into memory once

# Function to find all valid words from given letters
def four(fRack):
    """
    Finds all words from words.txt that can be formed using the given letters.
    """
    fRack_counter = Counter(fRack)  # Convert letters to Counter for quick comparison
    return [word for word in wordMaster if not Counter(word) - fRack_counter]

print("---------TEST FOUR-----------")
print("Below are words that can be created from the letters in the word 'retains':")
result, duration = timeFunction(four, "retains")
print(result, f"Time taken: {duration:.6f} seconds\n")

# Function for Spelling Bee word generation (same logic as four)
def five(fRack):
    """
    Finds valid words from words.txt that can be made with Spelling Bee rules.
    """
    return four(fRack)  # Reusing four() as it does the same job

print("---------TEST FIVE-----------")
print("Below are words that can be created from the Spelling Bee letters 'l'a'b'c'i'n'r':")
result, duration = timeFunction(five, "labcinr")
print(result, f"Time taken: {duration:.6f} seconds\n")

# Load dictionary file at the beginning for efficiency
try:
    with open(file_path, "r") as f:
        words = f.read().split()  # Read words into a list
    print("✅ Successfully loaded words.txt")
except FileNotFoundError:
    print(f"❌ Error: words.txt file not found at {file_path}")
