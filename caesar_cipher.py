def shift(letter, n):
    unicode_value = ord(letter) + n

    if(unicode_value > 126):
        difference = unicode_value - 126
        unicode_value = 32+difference

    if(unicode_value < 32):
        difference = 32 - unicode_value
        unicode_value = 126 - difference

    return chr(unicode_value)

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

    return result

secret_message = "encryption is fun"
encrypted_message = encrypt(secret_message, 5)

print(encrypted_message)
print(decrypt(encrypted_message, -5))


with open('caesar_sample_run.txt', 'w') as f:
    f.write(encrypted_message + "\n")
    f.write(decrypt(encrypted_message, -5))
