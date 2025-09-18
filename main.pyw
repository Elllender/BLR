from tkinter import NSEW, SOLID, StringVar, IntVar, RAISED, E, NS
from tkinter import Tk
from tkinter import ttk
from os import listdir
from secrets import SystemRandom
from PIL import Image, ImageTk

crpg = SystemRandom()

def buttnf():

    if checkbuttonvariable.get() == 1:
        randomvalue = crpg.choice(names_whitelist).upper()
        while labeltextvariable.get().upper() == randomvalue:
            randomvalue = crpg.choice(names_whitelist).upper()
        labeltextvariable.set(randomvalue)
    else:
        randomvalue = crpg.choice(names).upper()
        while labeltextvariable.get().upper() == randomvalue:
            randomvalue = crpg.choice(names).upper()
        labeltextvariable.set(randomvalue)

    image = Image.open(f"portraits-f/{labeltextvariable.get()}.jpg")
    image = ImageTk.PhotoImage(image)

    labelim.config(image=image)
    labelim.image = image

files = listdir('portraits/')

names = []

for file in files:
    names.append(file.split('.')[0])

names_whitelist = None

with open('whitelist.txt', 'r', encoding='utf-8') as f:
    names_whitelist = f.readlines()

names_whitelist = [x.replace('\n', '') for x in names_whitelist]

root = Tk()

width, height = 382, 495

s = (1920-width)/2, (1080-height)/2
s = round(s[0]), round(s[1])

root.geometry(f"{width}x{height}+{s[0]}+{s[1]}")
root.title("BLR")
#   root.configure(background="LightGrey")
root.iconbitmap(default="i.ico")

ttk.Style().theme_use("clam")

root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=0, weight=1)

# ttk styles
s = ttk.Style()
s.configure("My.TFrame", background="LightGray")
s.configure("My.TButton", font=("Arial", 24, "bold"), background="#E0E0E0", foreground="Crimson")
s.configure("MyText.TLabel", font=("Arial", 16, "bold"), background="whitesmoke")
s.configure("MyImage.TLabel", font=("Arial", 16, "bold"), background="LightGray", foreground="whitesmoke")
s.configure("My.TCheckbutton", font=("Arial", 12, ), background="LightGray", ) #anchor="center"

s.map("My.TCheckbutton", background=[('active', 'LightGray')])
# ttk styles

labeltextvariable = StringVar(value=crpg.choice(names).upper())
checkbuttonvariable = IntVar(value=1)

# frame
frame = ttk.Frame(root, borderwidth=0, relief=SOLID, style="My.TFrame")

for y in range(0, 3):
    for x in range(0, 2):
        frame.columnconfigure(index=x, weight=1)
        frame.rowconfigure(index=y, weight=1)

frame.grid(row=0, column=0, sticky=NSEW, padx=3, pady=3)
# frame

# button
btn = ttk.Button(frame, text="CHOOSE", style="My.TButton", takefocus=False, cursor="hand2", command=buttnf)
btn.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=4, pady=4)
# button

# labeltext
label = ttk.Label(frame, textvariable=labeltextvariable, style="MyText.TLabel", anchor="center", width=16, borderwidth=1, relief=RAISED)
label.grid(row=1, column=0, sticky=NSEW, padx=4)
# labeltext

# labelimage
image = Image.open(f"portraits-f/{labeltextvariable.get()}.jpg")
image = ImageTk.PhotoImage(image)

labelim = ttk.Label(frame, image=image, anchor="center", style="MyImage.TLabel") #style="My.TLabel"
labelim.grid(row=0, column=0, columnspan=2, sticky=NSEW)
# labelimage

# checkbutton
chbtn = ttk.Checkbutton(frame, text="whitelist", variable=checkbuttonvariable, takefocus=False, style="My.TCheckbutton", width=10, cursor="hand2")
chbtn.grid(row=1, column=1, sticky=NS, padx=4)
# checkbutton

root.resizable(False,False)
root.mainloop()