import time

def printDots():
    i = 0
    while i < 30:
        print(".", end = " ")
        time.sleep(0.03)
        i = i + 1
    
   
def encrypt(stringToEncrypt, shiftAmount):
    stringToEncrypt = stringToEncrypt.upper()
    encryptedString = ""

    for currentCharacter in stringToEncrypt:
        position = alphabet.find(currentCharacter)
        newPosition = position + shiftAmount
        encryptedString = encryptedString + alphabet[newPosition]

    return encryptedString
    
def decrypt(stringToEncrypt, shiftAmount):
    
    stringToEncrypt = stringToEncrypt.upper()
    decryptedString = ""

    for currentCharacter in stringToEncrypt:
        position = alphabet.find(currentCharacter)
        newPosition = position - shiftAmount
        decryptedString = decryptedString + alphabet[newPosition]
    return decryptedString





alphabet = "ABCDEFGHIJKLMNOPQRSTUVXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

printDots()
print("You have reached Top Secret National Security Agency tool")
printDots()
print("\n")

inputMessage = input("Please enter a message:")
secretKey = int(input("Please enter a whole number from 1-25 as a secret key:"))               
choice = input("Do you want to encrypt[e] or decrypt[d] message?")

printDots()
printDots()
print("\n")

if choice == 'e':
    message = encrypt(inputMessage, secretKey)
    print("Your encrypted message:", message)
elif choice == 'd':
    message = decrypt(inputMessage, secretKey)
    print("Your decrypted message:", message)
else:
    print("Wrong input. Are you just a kiddie?")



print("Disconnecting...")






