def caesar(text, shift, encrypt=True):
    
    if not isinstance(shift, int):
        return 'Shift must be an ineteger value.'
    if shift < 1 or shift > 25:
        return 'Shiftmust be a integer between 1 and 25.'
    
    alphabet = 'abcdefghijklmnopqrstuvwxynz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)


if __name__ == "__main__":
    
    encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
    decrypted_text = decrypt(encrypted_text, 13)
    print(decrypted_text)
