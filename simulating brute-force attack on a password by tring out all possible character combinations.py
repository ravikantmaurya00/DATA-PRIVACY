import itertools
import string
import time

# Function to perform brute-force attack on the given password
def brute_force_attack(target_password):
    # Define the character set to use for the attack: 
    # This includes lowercase letters, uppercase letters, digits, and punctuation
    charset = string.ascii_letters + string.digits + string.punctuation
    
    # Start a timer to measure how long the attack takes
    start_time = time.time()
    
    # Iterate over all possible lengths for the password (from 1 to the length of the target password)
    for length in range(1, len(target_password) + 1):
        # Generate all possible combinations of characters of the given length
        for attempt in itertools.product(charset, repeat=length):
            # Convert the tuple (which is generated by itertools.product) to a string
            attempt_password = ''.join(attempt)
            
            # Check if the generated password matches the target password
            if attempt_password == target_password:
                # Calculate the elapsed time for the brute-force attack
                elapsed_time = time.time() - start_time
                # Output the found password and the time it took to find it
                print(f"Password found: {attempt_password}")
                print(f"Time taken: {elapsed_time:.2f} seconds")
                return  # Exit the function since the password has been found
    
    # If no match was found, print that the password could not be cracked
    print("Password not found.")

# Example usage
if __name__ == "__main__":
    # Take the target password as user input
    target_password = input("Enter the password to simulate brute-force attack: ")
    
    # Notify user that the brute-force attack is starting
    print("Starting brute-force attack...")
    # Call the brute-force attack function to try and guess the password
    brute_force_attack(target_password)