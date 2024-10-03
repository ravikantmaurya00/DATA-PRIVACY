import random

def load_words():
   
    return [
        "apple", "banana", "cherry", "date", "elderberry", 
        "fig", "grape", "honeydew", "kiwi", "lemon", 
        "mango", "nectarine", "orange", "papaya", "quince", 
        "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
        "watermelon"
    ]

def generate_password(words, word_count=8):
    
    if len(words) < word_count:
        print("Not enough words to generate the password.")
        return None
    return ' $ '.join(random.sample(words, word_count))

if __name__ == "__main__":

    words = load_words()

    password = generate_password(words, word_count=8)
    
    if password:
        print(f"Generated password: {password}")