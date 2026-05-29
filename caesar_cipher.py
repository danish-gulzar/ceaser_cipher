# DecodeLabs Cybersecurity Internship - Project 2
# Basic Encryption & Decryption — Caesar Cipher


def caesar_cipher(text, shift):
    """
    Encrypt or decrypt text using Caesar cipher.
    
    Args:
        text: The text to encrypt/decrypt
        shift: The number of positions to shift (positive for encryption, negative for decryption)
    
    Returns:
        The encrypted/decrypted text
    """
    result = ""
    
    for char in text:
        if char.isupper():
            # Shift uppercase letters
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            # Shift lowercase letters
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def main():
    # Example usage
    message = "I'm a Hacker"
    shift = 3
    
    encrypted = caesar_cipher(message, shift)
    decrypted = caesar_cipher(encrypted, -shift)
    
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    main()
