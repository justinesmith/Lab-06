def password_encoder(password):
    new_password = ''
    for i in password:
        new_char = str((int(i)+3) % 10)
        new_password += new_char
    return new_password

def password_decoder(password):
    decoded_pass = ""
    for i in password:
        new_char = str((int(i)-3))
        decoded_pass += new_char
    return decoded_pass

print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")

program_on = True
while True:
    option = int(input("Please enter an option: "))
    if option == 1:
        first_password = str(input("Please enter your password to encode: "))
        encoded_password = password_encoder(first_password)
        print("Your password has been encoded and stored!")
        program_on = True

    if option == 2:
        decoded = password_decoder(encoded_password)
        print("The encoded password is", encoded_password + ", and the original password is", decoded)
    if option == 3:
        program_on = False
        break
