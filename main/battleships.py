# Imports
from tkinter import *
import random as ran

# enemy ai
position1x = ran.randint(0, 9)
position1y = ran.randint(0, 9)
position2x = ran.randint(0, 9)
position2y = ran.randint(0, 9)
position3x = ran.randint(0, 9)
position3y = ran.randint(0, 9)

# Make list so you can crossrefrence later with player actions
enemyX = [position1x, position2x, position3x]
enemyY = [position1y, position2y, position3y]

# For functions to do with player actions and game function later
NumEnemy = 3
Hits = 0
Ammo = 5
PlayerLose = False
AmmoTxt = "Ammo: "
# colours (taken from cattpuccin mocha colour scheme https://catppuccin.com/palette/)
BgColour = "#1e1e2e"
BgColour1 = "#9399b2"
StColourM = "#f4dbd6"
StColourH = "#ed8796"
StColourW = "a6da95"
TxtColour = "#cdd6f4"
TxtColour1 = "#5b6078"

# font
MainFont = ["JetBrains Mono", "13"]
TitleFont = ["JetBrains Mono", "17"]

# for debugging
print(position1x, position1y, position2x, position2y, position3x, position3y)

# window setup
root = Tk()

# create a basic window to host the game in
root.configure(bg=BgColour, border=5)

# set window title
root.title("BATTLESHIPS")

# set window size
root.geometry("780x390")

# create grid
for row in range(10):
    for col in range(10):
        btn = Button(root, bg=BgColour1, fg=TxtColour, font=MainFont,
                     text=f"{row},{col}", width=1, height=1)
        btn.grid(row=row, column=col, padx=0, pady=0)

# Game title
Title = Label(bg=BgColour1, fg=TxtColour, text="BATTLESHIPS", font=TitleFont)

Title.grid(row=0, column=10, columnspan=2)

# Hit status
Status = Label(bg=BgColour1, fg=TxtColour, text="normal", font=MainFont)

Status.grid(row=2, column=10, columnspan=2)


def update():
    AmmoCount.configure(text=Ammo)


# Ammo counter
AmmoCount = Label(bg=BgColour1, fg=TxtColour, text="Ammo = 5")

AmmoCount.grid(row=4, column=10, columnspan=2)

# string variables
X_var = IntVar()

Y_var = IntVar()

# actual function


def PlayerMove():
    global PlayerLose
    global Ammo
    global Hits
    if Ammo <= 0:  # checks if player has ammo
        Status.configure(bg=StColourH, fg=TxtColour1, text="You Lose")
    else:
        global enemyX
        global enemyY
        try:  # checks if X&Y are intigers
            x = X_var.get()
            y = Y_var.get()
            if x <= 9 and x >= 0 and y <= 9 and y >= 0:  # Check for invalid coordinates
                if x in enemyX and y in enemyY:  # checks to see if PlayerMove is a hit
                    Ammo = Ammo - 1  # gives you less ammo
                    print("hit")  # more debugging
                    Hits = Hits + 1  # for win condition later
                    print("current hits: ", Hits)
                    Status.configure(bg=StColourH, fg=TxtColour1, text="hit")
                    if Hits == NumEnemy:  # win condition
                        Status.configure(
                            bg=StColourW, fg=TxtColour1, text="you win")
                    else:
                        pass
                else:  # miss
                    Ammo = Ammo - 1
                    print("miss")
                    Status.configure(bg=StColourM, fg=TxtColour1, text="Miss")
                if Ammo == 0:  # lose condition
                    PlayerLose = True
                else:
                    pass
            else:
                print("Invalid number")
                Status.configure(bg=StColourH, fg=TxtColour1,
                                 text="Number to big/small")
        except TclError:
            print("not a nummber")
            Status.configure(bg=StColourH, fg=TxtColour1, text="Not a number")

    AmmoCount.configure(text=(AmmoTxt, Ammo))  # ammo counter math W.I.P


# player inputs
Entry1Label = Label(root, text="enter x coordinate",
                    font=MainFont, bg=BgColour1, fg=TxtColour,)

Entry2Label = Label(root, text="enter y coordinate",
                    font=MainFont, bg=BgColour1, fg=TxtColour)

Entry1 = Entry(root, textvariable=X_var, font=MainFont,
               bg=BgColour1, fg=TxtColour)

Entry2 = Entry(root, textvariable=Y_var, font=MainFont,
               bg=BgColour1, fg=TxtColour)

if PlayerLose is False:
    Submit = Button(root, text="Submit", bg=BgColour1,
                    fg=TxtColour, command=PlayerMove)
    Submit.grid(row=9, column=10, columnspan=2)
else:
    pass

Entry1Label.grid(row=7, column=10)
Entry2Label.grid(row=8, column=10)
Entry1.grid(row=7, column=11)
Entry2.grid(row=8, column=11)

# Window end
root.mainloop()
