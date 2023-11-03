import sys

'''
    Encodes an alphabetic Plaintext Message using Viegnere Cipher
'''
def vigenere_encoder(string, key):
    cipher_text = []
    klength = len(key)
    kcount = 0
    for i in range(len(string)):
        if string[i].isspace():
            cipher_text.append(string[i])
        else:
            x = (((ord(string[i])) + (ord(key[(kcount % klength)]))) % 26) + ord('A')
            kcount += 1
            cipher_text.append(chr(x))
    return ("".join(cipher_text))


'''
    Decodes a Vigenere Cipher Encrypted Message
'''
def vigenere_decoder(string, key):
    orig_text = []
    klength = len(key)
    kcount = 0
    for i in range(len(string)):
        if string[i].isspace():
            orig_text.append(string[i])
        else: 
            x = (((ord(string[i])) - (ord(key[(kcount % klength)]))) % 26) + ord('A')
            kcount += 1
            orig_text.append(chr(x))
    return ("".join(orig_text))
    

if __name__ == "__main__":
    
    lines = ""
    key = []

    if len(sys.argv) != 4:
        print("Usage: python3 vignere_cipher_encoder.py filename key encode/decode")
        exit(1)
    
    key_string = sys.argv[2]
    
    if not key_string.isupper():
        print("All letters in key must be UPPER CASE")
        exit(1)
    
    key = list(key_string)
        
    try:
        f = open(sys.argv[1], "r")
        file_lines = f.readlines()
    except:
        print("Cannot read in file. File must exist")
        exit(1)

    for line in file_lines:
        lines = lines + line
        
    if sys.argv[3] == "encode":
        encrypted_text = vigenere_encoder(lines, key)
        print("Encoded Message is:")
        print(encrypted_text) 
    elif sys.argv[3] == "decode":
        orig_text = vigenere_decoder(lines, key)
        print("Decoded Message is:")
        print(orig_text)
    else:
        print("Unknown command. Inputted command must be 'decode' or 'encode'")
    
    
    