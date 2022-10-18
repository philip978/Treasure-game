print("you have arrived on a treasure land!")
print("your mission is to find the treasure!")
y = 0
z = 0
x = input("you are in front of two doors,Do yu wanna go left or right?\n")
if x.lower() == "left":
    print("0uch!!There is a room full of fire,you are wasted!")
elif x.lower() == "right":
    y = input("you have reached a room half filled with water,Do you wanna swim or wait?\n")
    if y.lower() == "swim":
        print("Oooppss!!The room was filled after a short while,you drowned!")
    elif y.lower() == "wait":
        z = input(
            "A boat arrived and sent you directly into cave\nThere are 3 boxes,red,yellow and green.\nYou can only make one choice.\n")
        if z.lower() == "green":
            print("Eyy!!box was full of snakes you were bitten,You lose!")
        elif z.lower() == "yellow":
            print("OW!!box was empty,You lose!")
        elif z.lower() == "red":
            print("Aaahhh!Congratulations!You found the the treasure,You win!")
        else:
            print("incorrect input,try again!")

    else:
        print("incorrect input.Try again!")

else:
    print("incorrect input.Try again!")
