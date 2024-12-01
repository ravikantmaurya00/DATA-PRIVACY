import hashlib
import requests
import csv

# Function to create a CSV file with usernames and passwords
def create_csv(filename, data):
    """
    Creates a CSV file with the provided username-password data.
    
    Parameters:
        - filename: Name of the CSV file to create (string).
        - data: List of dictionaries with 'username' and 'password' keys.
    """
    # Define the column headers for the CSV file
    fieldnames = ['username', 'password']
    
    # Open the CSV file in write mode with UTF-8 encoding and no extra blank lines between rows
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        # Create a DictWriter object that will write the dictionaries as rows
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header row to the CSV file (the field names)
        writer.writeheader()
        
        # Loop through the data list and write each username-password pair to the CSV
        for row in data:
            writer.writerow(row)
    
    # Inform the user that the file has been created successfully
    print(f"CSV file '{filename}' created successfully!")

# Example usage
if __name__ == "__main__":
    # Sample data: list of dictionaries with 'username' and 'password' keys
    users = [
        {"username": "user1", "password": "password123"},
        {"username": "user2", "password": "securepass456"},
        {"username": "user3", "password": "admin@2023"},
        {"username": "user4", "password": "Ravi@2023"},
        {"username": "user5", "password": "Ram@2023"},
        {"username": "user6", "password": "sahil23@2023"},
        {"username": "user7", "password": "ravi@2023"},
        {"username": "user8", "password": "Ravi@123"},
        {"username": "user9", "password": "Ravikant@63806"},
        {"username": "user10", "password": "abc@12345678"},
        {"username": "user11", "password": "abcd@1234"},
        {"username": "user12", "password": "ram@2024"},
        {"username": "user13", "password": "765der@"},
        {"username": "user14", "password": "admin@2023"},
        {"username": "user15", "password": "admin@2023"}
    ]
    
    # File name for the CSV (this will be the name of the file saved on disk)
    csv_filename = "Generally_used_passwords.csv"
    
    # Call the function to create the CSV file with the sample data
    create_csv(csv_filename, users)


# Function to check if the password is part of a data breach using "Have I Been Pwned" API
def check_password_breach(password):
    """
    Checks whether the given password has been part of a known data breach
    using the "Have I Been Pwned" API.
    
    Parameters:
        - password: The password to check.
    
    Returns:
        - True if the password has been found in a data breach, 
        - False if not, or None if there's an error.
    """
    # Compute the SHA-1 hash of the password
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Send the first 5 characters to the API
    first_five = sha1_hash[:5]
    remaining_hash = sha1_hash[5:]
    
    # Send GET request to the API with the first 5 characters of the hash
    url = f"https://api.pwnedpasswords.com/range/{first_five}"
    response = requests.get(url)
    
    # Check if the remaining hash is in the response (indicating a match)
    if response.status_code == 200:
        if remaining_hash in response.text:
            return True  # Password found in breach
        else:
            return False  # Password not found in breach
    else:
        print("Error fetching data from Have I Been Pwned API")
        return None


# Function to check usernames and passwords from a file
def check_file_for_breaches(file_path):
    """
    Reads a CSV file with usernames and passwords, checks each password 
    for breaches using the "Have I Been Pwned" API, and prints the results.
    
    Parameters:
        - file_path: The path to the CSV file containing username-password pairs.
    """
    # Open the CSV file for reading
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        # Loop through each row (username and password pair)
        for row in reader:
            username, password = row
            
            # Check the password against the API
            print(f"Checking password for {username}...")
            if check_password_breach(password):
                print(f"Password for {username} has been pwned!")
            else:
                print(f"Password for {username} has NOT been pwned.")

# Example usage with user input
if __name__ == "__main__":
    # Path to the file containing usernames and passwords (use the file created earlier)
    file_path = "Generally_used_passwords.csv"
    
    # Check each username and password pair for data breaches
    check_file_for_breaches(file_path)
