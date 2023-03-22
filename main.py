# Justine Smith
def password_encoder(password):
    new_password = ''   
    for i in password:
        new_char = str((int(i)+3) % 10)     # adds 3 to each character in password, and makes sure each character is not more than 2 digits
        new_password += new_char
    return new_password

def password_decoder(password):
    decoded_pass = ""
    for i in password:
        new_char = str((int(i)-3))   # subtracts 3 from each character in passwoard and makes sure its not negative and not more than 2 digits
        decoded_pass += new_char
    return decoded_pass


program_on = True
while True:
    print("""Menu    # menu
-------------
1. Encode
2. Decode
3. Quit
""")
    option = int(input("Please enter an option: "))
    if option == 1:       # if option is 1, encodes password and stores it
        first_password = str(input("Please enter your password to encode: "))
        encoded_password = password_encoder(first_password)
        print("Your password has been encoded and stored!")
        program_on = True

    if option == 2:     # if option is 2, prints the encoded password and the decoded password
        decoded = password_decoder(encoded_password)
        print("The encoded password is", encoded_password + ", and the original password is", decoded)
    if option == 3:    # quits program
        program_on = False
        break
