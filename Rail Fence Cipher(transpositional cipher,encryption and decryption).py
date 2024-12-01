# Function to encrypt the plaintext using Rail Fence Cipher
def encrypt(plaintext, rails):
    """
    Encrypts the plaintext using the Rail Fence Cipher with the specified number of rails.
    Parameters:
        - plaintext: The text to encrypt.
        - rails: The number of rails (zigzag rows) in the cipher.
    Returns:
        - encrypted_text: The resulting encrypted text.
    """
    # Create a 2D list (matrix) to represent the rail fence
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    
    # Variables to track the current row and direction of movement (zigzag pattern)
    row, step = 0, 1
    
    # Populate the fence with plaintext characters in a zigzag manner
    for col in range(len(plaintext)):
        fence[row][col] = plaintext[col]  # Place character in the current row and column
        
        # Change direction at the top or bottom rail
        if row == 0:
            step = 1  # Move down
        elif row == rails - 1:
            step = -1  # Move up
        
        row += step  # Move to the next row based on the direction
    
    # Concatenate all characters from the fence row by row to form the encrypted text
    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

# Function to decrypt the ciphertext using Rail Fence Cipher
def decrypt(ciphertext, rails):
    """
    Decrypts the ciphertext encrypted using the Rail Fence Cipher with the specified number of rails.
    Parameters:
        - ciphertext: The encrypted text to decrypt.
        - rails: The number of rails (zigzag rows) used during encryption.
    Returns:
        - decrypted_text: The resulting decrypted text.
    """
    # Create a 2D list (matrix) to represent the rail fence
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    # Variables to track the current row and direction of movement (zigzag pattern)
    row, step = 0, 1
    
    # Mark the zigzag positions with a placeholder ('*')
    for col in range(len(ciphertext)):
        fence[row][col] = '*'
        
        if row == 0:
            step = 1  # Move down
        elif row == rails - 1:
            step = -1  # Move up
        
        row += step  # Move to the next row based on the direction
    
    # Fill the zigzag positions with characters from the ciphertext
    index = 0
    for row in range(rails):
        for col in range(len(ciphertext)):
            if fence[row][col] == '*':  # If marked, place the next ciphertext character
                fence[row][col] = ciphertext[index]
                index += 1
    
    # Read the characters in the zigzag pattern to reconstruct the plaintext
    decrypted_text = ''
    row, step = 0, 1
    for col in range(len(ciphertext)):
        decrypted_text += fence[row][col]  # Append character to the decrypted text
        
        if row == 0:
            step = 1  # Move down
        elif row == rails - 1:
            step = -1  # Move up
        
        row += step  # Move to the next row based on the direction
    
    return decrypted_text

# Example usage with user input
if __name__ == "__main__":
    # Get user input
    plaintext = input("Enter the text to encrypt: ")  # Text to be encrypted
    rails = int(input("Enter the number of rails: "))  # Number of rails (rows) for the zigzag pattern

    # Encrypt the input text
    encrypted = encrypt(plaintext, rails)
    print(f"Encrypted Text: {encrypted}")  # Display the encrypted text

    # Decrypt the text back
    decrypted = decrypt(encrypted, rails)
    print(f"Decrypted Text: {decrypted}")  # Verify that the decrypted text matches the original plaintext
