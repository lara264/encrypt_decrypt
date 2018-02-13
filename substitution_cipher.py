alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "qwertyuioplkjhgfdsazxcvbnm "

def encrypt(message):
    result = ""

    for letter in message:
        location = alphabet.find(letter)
        result += key[location]

    return result

def decrypt(message):
    result = ""

    for letter in message:
        location = key.find(letter)
        result += alphabet[location]

    return result


unencrypted_message = "encryption is fun"
encrypted_message = encrypt(unencrypted_message)

print(unencrypted_message)
print(encrypted_message)

print(decrypt(encrypted_message))


