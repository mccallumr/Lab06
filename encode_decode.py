# Rachel McCallum

def encode(numerical_str):
    length = len(numerical_str)
    numerical_int = int(numerical_str)
    addend = int("3"*length)
    numerical_int += addend
    numerical_string = str(numerical_int)
    return numerical_string

#decode() function made by Thomas Crespo
def decode(enpassword):
    resul = ''
    temp = 0
    for num in enpassword:
        temp = int(num) - 3
        if temp < 0:
            temp = temp + 10
        resul = resul + str(temp)
    return resul

def main():
    while True:
        print(
"""
Menu
-------------
1. Encode
2. Decode
3. Quit
"""
)
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            #Added print statement for return with the decode function inside
            print('The encoded password is ' + encoded_password + ', and the original password is ' + decode(encoded_password) + '.')
        elif option == 3:
            break


if __name__ == '__main__':
    main()
