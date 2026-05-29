# Simple Caesar Cipher

A Python implementation of the Caesar cipher, a classic substitution cipher technique.

## What is Caesar Cipher?

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## Features

- Encrypt text using a shift value
- Decrypt text by using the negative of the shift value
- Supports both uppercase and lowercase letters
- Preserves non-alphabetic characters (spaces, punctuation, etc.)
- Simple and easy to understand implementation

## Usage

### Running the script

```bash
python caesar_cipher.py
```

### Using the function in your code

```python
from caesar_cipher import caesar_cipher

# Encrypt a message
encrypted = caesar_cipher("Hello, World!", 3)
print(encrypted)  # Output: Khoor, Zruog!

# Decrypt a message
decrypted = caesar_cipher(encrypted, -3)
print(decrypted)  # Output: Hello, World!
```

## Example Output

```
Original: I'm a Hacker
Encrypted: L'p d Kdfnhu
Decrypted: I'm a Hacker
```

## How It Works

The cipher works by shifting each letter in the text by a specified number of positions:

- For uppercase letters: `(ord(char) - 65 + shift) % 26 + 65`
- For lowercase letters: `(ord(char) - 97 + shift) % 26 + 97`
- Non-alphabetic characters remain unchanged

The modulo operation ensures that the shift wraps around the alphabet (e.g., 'z' shifted by 1 becomes 'a').

## Requirements

- Python 3.x

## License

This project is open source and available for educational purposes.
