import sys

# Define printable character range
LOWER_BOUND = 0x20
UPPER_BOUND = 0xFF
CHAR_RANGE = UPPER_BOUND - LOWER_BOUND + 1  # Total number of characters in range

def caesar_cipher(text: str, key: int, encrypt: bool) -> str:
    """
    input given text
    input shift value
    declare true or false value for encryption/decryption
    """
    if not encrypt:
        key = -key  # Reverse the shift for decryption

    transformed = []
    for char in text:
        char_code = ord(char)
        if LOWER_BOUND <= char_code <= UPPER_BOUND:
            # Apply shift within the printable range
            new_code = (char_code - LOWER_BOUND + key) % CHAR_RANGE + LOWER_BOUND
            transformed.append(chr(new_code))
        else:
            # Keep character unchanged if it's out of the range
            transformed.append(char)
    
    return "".join(transformed)

def process_file(filename: str, key: int, encrypt: bool):
    """
    input given text
    input shift value
    declare true or false value for encryption/decryption
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Encrypt or decrypt content
        processed_content = caesar_cipher(content, key, encrypt)
        
        # Create output filename
        mode = "encrypted" if encrypt else "decrypted"
        output_filename = f"{filename}.{mode}.txt"
        
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(processed_content)
        
        print(f"Successfully {mode} file saved as: {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python caesar_cipher.py <filename> <key> <mode>")
        print("Mode should be 'encrypt' or 'decrypt'.")
        sys.exit(1)

    filename = sys.argv[1]
    key = int(sys.argv[2])
    mode = sys.argv[3].lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Error: Mode must be 'encrypt' or 'decrypt'.")
        sys.exit(1)

    process_file(filename, key, mode == "encrypt")
