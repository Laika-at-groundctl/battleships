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

# colours (taken from cattpuccin mocha colour scheme https://catppuccin.com/palette/)
BgColour = "#1e1e2e"
TxtColour = "#cdd6f4"
BgColour1 = "#9399b2"

# font
MainFont = ["JetBrains Mono", "13"]

# for debugging
print(position1x, position1y, position2x, position2y, position3x, position3x)

# window setup
root = Tk()

# create a basic window to host the game in
root.configure(bg=BgColour, border=5)

# set window title
root.title("BATTLESHIPS")

# set window size
root.geometry("700x700")

# create grid
for row in range(10):
    for col in range(10):
        btn = Button(root, bg=BgColour1, fg=TxtColour, font=MainFont,
                     text=f"{row},{col}", width=1, height=1)
        btn.grid(row=row, column=col, padx=0, pady=0)

# string variables
X_var = StringVar()

Y_var = StringVar()

# player inputs
Entry1Label = Label(root, text="enter x coordinate",
                    font=MainFont, bg=BgColour1, fg=TxtColour,)

Entry2Label = Label(root, text="enter y coordinate",
                    font=MainFont, bg=BgColour1, fg=TxtColour)

Entry1 = Entry(root, textvariable=X_var, font=MainFont,
               bg=BgColour1, fg=TxtColour)

Entry2 = Entry(root, textvariable=Y_var, font=MainFont,
               bg=BgColour1, fg=TxtColour)

Entry1Label.grid(row=10, column=10)
Entry2Label.grid(row=11, column=10)
Entry1.grid(row=10, column=11)
Entry2.grid(row=11, column=11)
# Window end
root.mainloop()
