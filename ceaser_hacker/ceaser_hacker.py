import sys, random, string

symbol_list = list(string.ascii_lowercase)

def main():
    while True:
        print("What do you want, (e)ncryt or (d)ecrypt?")
        response = input(">  ")
        if response.lower().startswith("e"):
            mode = "Encrypt"
            break
        elif response.lower().startswith("d"):
            mode = "Decrypt"
            break
        else:
            continue
    print(f"Enter the text you wish to {mode}")
    response = input("\n>")
    response_list = [i for i in response]
    for key in range(0,25):
        output = []
        for j in response_list:
            if j in symbol_list:
                index = symbol_list.index(j)
                x = index + key
                if x<=25:
                    pass
                elif x>25:
                    x = x % 25
                output.append(symbol_list[x])
            else:
                output.append(j)
        print("".join(output))
#abcd efgh ijkl mnop qrst uvwx yz

if __name__ == '__main__':
    main()