from random import randint

ALPHABET = [
        "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U",
        "V", "W", "X", "Y", "Z"
]

def draw_letters():
    ten_strings = []
    # Pool dictionary to keep count of letters
    LETTER_POOL = {
        "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3,
        "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6,
        "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4,
        "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1
    }

    # While ten_strings doesn't have 10 letters -> execute loop
    while len(ten_strings) < 10:
        num = randint(0, 25)
        letter = ALPHABET[num]
        available = LETTER_POOL[letter]
        
        print(f"Letter: {letter} Pool amount: {available}")

        # If the pool has letters available -> add to ten_strings
        if available > 0:
            LETTER_POOL[letter] = available - 1
            ten_strings.append(letter)
    
    print(f"Ten Strings: {ten_strings}")
    return ten_strings

def uses_available_letters(word, letters):
    letter_pool = get_letter_pool(letters)
    
    # Check each letter in the word
    for letter in word.upper():  # Convert to uppercase
        if letter in letter_pool and letter_pool[letter] > 0:
            letter_pool[letter] -= 1
        else:
            return False
    
    return True

# Helper function to create letter pool dictionary
def get_letter_pool(letter_list):
    count_dict = {}
    for letter in letter_list:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass