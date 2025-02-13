🔐 Simple Encryption & Decryption Program
This is a fun and simple encryption program that uses a randomly shuffled character mapping to encode and decode messages. The encryption process replaces each character in your message with a randomly assigned counterpart, making it impossible to read without the key.

🚀 Features
✅ Encrypts messages using a randomized key
✅ Decrypts messages back to the original text
✅ Runs continuously until you type "exit"
✅ Supports letters, numbers, punctuation, and spaces

🛠 How It Works
The program creates two lists:
chars: Contains all letters, digits, punctuation, and spaces
key: A shuffled version of chars, used for substitution
When you enter a message:
Each character is replaced with its corresponding value from key
This forms the cipher text (encrypted message)
The program can also decrypt the message using the same key

🏃‍♂️ How to Run
Copy and paste the Python code into a script (encryptor.py)
Run it in the terminal:
bash
Copy
Edit
python encryptor.py
Enter a message to encrypt
The program will show the cipher text and its decryption
Keep encrypting/decrypting or type "exit" to quit

🔄 Example
yaml
Copy
Edit
🔐 Enter a message to encrypt: Hello, world!
🔒 Cipher Text: G&//9<,Y/!9<U
🔓 Deciphered Text: Hello, world!
⚠️ Notes
Each session uses a different key, so cipher texts are unique every time
If you restart the program, you cannot decrypt old messages
Spaces and special characters are preserved
