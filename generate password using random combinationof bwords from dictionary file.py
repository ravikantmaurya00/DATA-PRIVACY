import random

# Predefined list of dictionary words (can be extended as needed)
dictionary_words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", 
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", 
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xylophone", "yellow", 
    "zucchini", "avocado", "blueberry", "cantaloupe", "dragonfruit", "apricot", "blackberry", 
    "coconut", "plum", "pear", "persimmon", "pomegranate", "jackfruit", "lychee", "fig", 
    "clementine", "pineapple", "watercress", "spinach", "lettuce", "tomato", "onion", 
    "garlic", "carrot", "broccoli", "cauliflower", "potato", "sweetpotato", "beet", "asparagus", 
    "peas", "artichoke", "celery", "pumpkin", "radish", "cucumber", "ginger", "chili", 
    "cilantro", "oregano", "parsley", "basil", "thyme", "rosemary", "sage", "tarragon", 
    "mint", "dill", "curry", "nutmeg", "cinnamon", "cardamom", "clove", "paprika", 
    "turmeric", "saffron", "vanilla", "chocolate", "coffee", "tea", "latte", "mocha", 
    "espresso", "cappuccino", "macchiato", "lemonade", "lime", "grapefruit", "orangeade", 
    "applejuice", "carrotjuice", "tomatojuice", "gingerale", "soda", "fizz", "milk", 
    "yogurt", "cheese", "butter", "cream", "icecream", "frozenyogurt", "popcorn", "chips", 
    "pretzel", "cookie", "brownie", "cake", "pie", "donut", "muffin", "cupcake", "pancake", 
    "waffle", "toast", "sandwich", "burger", "pizza", "pasta", "noodle", "spaghetti", 
    "lasagna", "meatball", "hotdog", "steak", "chicken", "fish", "salmon", "tuna", 
    "lobster", "shrimp", "crab", "clam", "oyster", "mussels", "sushi", "sashimi"
]

# Function to create a .txt file with dictionary words
def create_dict_txt(filename, words):
    """
    Creates a .txt file with the provided list of words.
    
    Parameters:
        - filename: The name of the .txt file to create (string).
        - words: List of words to write into the .txt file.
    """
    # Open the file in write mode and write each word from the dictionary list to it
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')  # Write each word on a new line
    
    # Print confirmation message after creating the file
    print(f"File '{filename}' created with dictionary words.")

# Example usage
if __name__ == "__main__":
    # File name for the .txt file to store the dictionary words
    txt_filename = "dictionary_words.txt"
    
    # Create the .txt file with the list of dictionary words
    create_dict_txt(txt_filename, dictionary_words)

    # Ask the user for the number of words they want in the password
    # This input will determine how many random words will be chosen for the password
    num_words = int(input("Enter the number of words you want in your password: "))
    
    # Function to generate a password from a dictionary file
    def generate_password(dictionary_file, num_words, separator="-"):
        """
        Generate a random password using words from the dictionary file.
        
        Parameters:
        - dictionary_file: Path to the text file containing a list of words.
        - num_words: The number of random words to include in the password (default: 4).
        - separator: The separator between words (default: "-").
        
        Returns:
        - A string representing the generated password.
        """
        # Read words from the dictionary file
        try:
            # Open the dictionary file and read the words into a list
            with open(dictionary_file, 'r') as file:
                words = [line.strip() for line in file.readlines()]
            
            # If the dictionary file is empty, raise an exception
            if len(words) == 0:
                raise ValueError("Dictionary file is empty.")
            
            # Randomly select the specified number of words from the dictionary
            selected_words = random.sample(words, num_words)
            
            # Join the selected words using the provided separator
            password = separator.join(selected_words)
            return password
        
        except FileNotFoundError:
            print(f"Error: The file '{dictionary_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Generate the password using the provided dictionary file and number of words
    dictionary_file = "dictionary_words.txt"  # Replace with the actual dictionary file path
    password = generate_password(dictionary_file, num_words, separator="-")
    
    # If a password was generated, print it
    if password:
        print(f"Generated Password: {password}")
