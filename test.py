import string
import random

# Generate character sets
chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
key = chars.copy()
random.shuffle(key)


def encrypt(text, key):
  """Encrypt the given text using the shuffled key."""
  return "".join(key[chars.index(letter)] for letter in text)


def decrypt(cipher_text, key):
  """Decrypt the given text using the shuffled key."""
  return "".join(chars[key.index(letter)] for letter in cipher_text)


# Loop for repeated encryption & decryption
while True:
  text = input("\n🔐 Enter a message to encrypt (or type 'exit' to quit): ")

  if text.lower() == "exit":
    print("👋 Goodbye!")
    break  # Exit the loop

  cipher_text = encrypt(text, key)
  decipher_text = decrypt(cipher_text, key)

  print(f"\n🔒 Cipher Text: {cipher_text}")
  print(f"🔓 Deciphered Text: {decipher_text}")
