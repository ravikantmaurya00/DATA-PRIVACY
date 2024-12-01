# Function to encrypt the plaintext
def encrypt(plaintext, shift):
    """
    Encrypts the given plaintext using a Caesar cipher with the specified shift.
    Parameters:
        - plaintext: The text to be encrypted.
        - shift: The number of positions each character should be shifted.
    Returns:
        - encrypted_text: The resulting encrypted text.
    """
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base ASCII value (uppercase: 65, lowercase: 97)
            shift_base = 65 if char.isupper() else 97
            # Perform the Caesar cipher shift within the alphabet range
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # If not a letter, keep the character unchanged (e.g., spaces, punctuation)
            encrypted_text += char
    return encrypted_text

# Function to decrypt the ciphertext
def decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using a Caesar cipher with the specified shift.
    Parameters:
        - ciphertext: The encrypted text to be decrypted.
        - shift: The number of positions each character was shifted during encryption.
    Returns:
        - decrypted_text: The resulting decrypted text.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base ASCII value (uppercase: 65, lowercase: 97)
            shift_base = 65 if char.isupper() else 97
            # Reverse the Caesar cipher shift to decrypt
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # If not a letter, keep the character unchanged
            decrypted_text += char
    return decrypted_text

# Example usage with user input
if __name__ == "__main__":
    # Get user input
    plaintext = input("Enter the text to encrypt: ")  # The text to be encrypted
    shift = int(input("Enter the shift value (integer): "))  # The Caesar cipher shift value

    # Encrypt the input text
    encrypted = encrypt(plaintext, shift)
    print(f"Encrypted Text: {encrypted}")  # Display the encrypted text

    # Decrypt the text back
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted Text: {decrypted}")  # Verify that the decrypted text matches the original
