import random, sys
import string

alphabets = list(string.ascii_lowercase)


def main():
    coded_text = []
    print("What do you want, Encrypt(e) or Decrypt(d)?")
    while True:
        response = input("> ")
        if response.startswith('e'):
            subject = "encrypt"
            break
        elif response.startswith('d'):
            subject = "decrypt"
            break
        else:
            print("Wrong input. Please enter either 'c' or 'd'")

    print(f"Enter the text you wish to {subject}.")
    text = input("> ")

    print("Please enter a key you wish to use between 0 and %s" % (len(alphabets) - 1))
    while True:
        key = (input("> "))
        if key.isdigit():
            key = int(key)
            break
        else:
            continue

    for i in text:
        if i in alphabets:
            x = int(alphabets.index(i))
            if subject == "encrypt":
                x += key
            elif subject == "decrypt":
                x -= key
            if int(x) <= 25:
                coded_text.append(alphabets[x])
            elif int(x) > 25:
                coded_text.append(alphabets[int(x % 25) - 1])
        elif i not in alphabets:
            coded_text.append(i)
    print("".join(coded_text))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit()  # When Ctrl-C is pressed, end the program.
