import art
# 🔐 Caesar Cipher Application by Kareem Tamer 👨‍💻✨
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
print("🌟 Welcome 👋 to the **Caesar Cipher Application** 🔐")
print("🔁 You can encode (🔏) or decode (🔓) messages safely and easily!\n")

goal = True

def encode(original_message, shift_amount):
    encrypted_message = ""
    for letter in original_message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            encrypted_message += alphabet[new_position]
        else:
            encrypted_message += letter
    print(f"\n🔐 Encoded message ⛓️: **{encrypted_message}**\n")

def decode(encrypted_message, shift_amount):
    decoded_message = ""
    for letter in encrypted_message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            decoded_message += alphabet[new_position]
        else:
            decoded_message += letter
    print(f"\n🔓 Decoded message ⛓️‍💥: **{decoded_message}**\n")

while goal:
    choose = input("🧭 Type 'encode' 🔏 to encrypt, or 'decode' 🔓 to decrypt:\n👉 ").lower()
    message = input("💬 Type your message:\n👉 ").lower()
    shift = int(input("🔢 Type the shift number (e.g. 3):\n👉 "))

    if choose == "encode":
        encode(message, shift)
    elif choose == "decode":
        decode(message, shift)
    else:
        print("❌ Invalid choice 😒. Please type 'encode' or 'decode'.\n")

    again = input("🔁 Do you want to go again? Type 'yes' ✅ or 'no' ❌:\n👉 ").lower()
    if again == "no":
        print("\n🙏 Thank you for using the Caesar Cipher App! Stay safe 🔒 & goodbye! 👋💫")
        goal = False
