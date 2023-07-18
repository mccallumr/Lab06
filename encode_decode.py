# Rachel McCallum

def encode(numerical_str):
    length = len(numerical_str)
    numerical_int = int(numerical_str)
    addend = int("3"*length)
    numerical_int += addend
    numerical_string = str(numerical_int)
    return numerical_string


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
            pass
        elif option == 3:
            break


if __name__ == '__main__':
    main()
