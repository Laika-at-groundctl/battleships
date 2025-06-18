# Imports
from tkinter import *
import random as ran
import time

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

# For a function later
NumEnemy = 3
hits = 0

# colours (taken from cattpuccin mocha colour scheme https://catppuccin.com/palette/)
BgColour = "#1e1e2e"
BgColour1 = "#9399b2"
StColourM = "#f4dbd6"
StColourH = "#ed8796"
TxtColour = "#cdd6f4"
TxtColour1 = "#5b6078"

# font
MainFont = ["JetBrains Mono", "13"]
TitleFont = ["JetBrains Mono", "17"]

# for debugging
print(position1x, position1y, position2x, position2y, position3x, position3x)

# window setup
root = Tk()

# create a basic window to host the game in
root.configure(bg=BgColour, border=5)

# set window title
root.title("BATTLESHIPS")

# set window size
root.geometry("800x500")

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

# string variables
X_var = IntVar()

Y_var = IntVar()

# actual function


def PlayerMove():

    # x = X_var.get()
    # y = Y_var.get()

    global enemyX
    global enemyY
    try:
        x = X_var.get()
        y = Y_var.get()
        if x <= 9 and x >= 0 and y <= 9 and y >= 0:
            if x in enemyX and y in enemyY:
                print("hit")
                global hits
                hits = hits + 1
                print("current hits: ", hits)
                Status.configure(bg=StColourH, fg=TxtColour1, text="hit")
                # time.sleep(100)
                # Status.configure(bg=BgColour1, fg=TxtColour, text="normal")
            else:
                print("miss")
                Status.configure(bg=StColourM, fg=TxtColour1, text="Miss")
        else:
            print("Invalid number")
            Status.configure(text="Number to big/small")
    except:
        print("not a nummber")
        Status.configure(text="Not a number")


# player inputs
Entry1Label = Label(root, text="enter x coordinate",
                    font=MainFont, bg=BgColour1, fg=TxtColour,)

Entry2Label = Label(root, text="enter y coordinate",
                    font=MainFont, bg=BgColour1, fg=TxtColour)

Entry1 = Entry(root, textvariable=X_var, font=MainFont,
               bg=BgColour1, fg=TxtColour)

Entry2 = Entry(root, textvariable=Y_var, font=MainFont,
               bg=BgColour1, fg=TxtColour)

Submit = Button(root, text="Submit", bg=BgColour1,
                fg=TxtColour, command=PlayerMove)

Entry1Label.grid(row=7, column=10)
Entry2Label.grid(row=8, column=10)
Entry1.grid(row=7, column=11)
Entry2.grid(row=8, column=11)
Submit.grid(row=9, column=10)

# player win condition
if hits == NumEnemy:
    print("You win")
else:
    pass

# Window end
root.mainloop()
