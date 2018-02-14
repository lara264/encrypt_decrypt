alphabet = ""
for i in range(32, 127):
    alphabet += chr(i)
print(alphabet)

key = ""
for n in alphabet:
    key = n + key
print(key)

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

with open("substitution_sample_run.txt", "w") as f:
    f.write(unencrypted_message)
    f.write(encrypted_message)
    f.write(decrypt(encrypted_message))


