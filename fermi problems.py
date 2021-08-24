import random as rd

x = ["golf balls", "litres of water", "xbox series x", "rubix cubes", "glasses", "packets of crisps", "houses", "playstation controllers", "mugs", "shoes"]
y = ["a yacht", "a ferrari", "an xbox series x", "a rubix cube", "a glass", "a wardrobe", "a packet of crisps", "pluto", "the statue of liberty", "a hand"]


def fermi ():
    print ("How many", rd.choice(x), "would fit into", rd.choice(y))


fermi()

while True:
    choice = input("Would you like to play again:")
    if choice == "YES".lower():
        fermi()
    else:
        print ("OK :__(")
        break
