# Rachel Young

def encode(num_string: str) -> str:
    encoded = ""
    for char in num_string:
        encoded += str((int(char) + 3) % 10)
    return encoded


def main():
    op = 1
    while op in range(1, 3):
        # print menu
        print("Password Encoder")
        print("----------------")
        print("0. Exit")
        print("1. Encode Password")
        print("2. Decode Password")

        # get user input
        op = int(input("Select an option: "))

        if op == 1:
            num_string = input("Enter a password to encode: ")
            print(f"Original password: {num_string}")
            print(f"Encoded password:  {encode(num_string)}")
        elif op == 2:
            num_string = input("Enter a password to decode: ")
            print(f"Original password: {num_string}")
            # print(f"Decoded password: {decode(num_string)}")
            print("hi")


if __name__ == "__main__":
    main()
