#part 2 of my programming course final
def main():
    name = input("Whats your name? ") #asking what your name is and storing it as a variable
    length = len(name) #counting the amount of letters

    if length % 2 == 0: #I wanted to use the modulo operator because if you divide a odd number in half, you get a remainer, if it's even, you don't!
        print("That's an even number of letters in your name")
    else:
        print("That's an odd number of letters in your name")
main()
