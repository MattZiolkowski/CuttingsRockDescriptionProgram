#! python3

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import Font
import tkinter.scrolledtext as tkst

##########
# Window #
##########

win = tk.Tk()

win.title("Cuttings Description BETA")

# Icon

win.wm_iconbitmap("CDicon.ico")

# String Varaible for radiobuttons

v = StringVar()

# Title font

helv36 = Font(family='Helvetica', size=25, weight='bold')

############
# Widgets: #
############

# Title
l1 = ttk.Label(win,text= "Cuttings Rock Description", font = helv36)

# Unit label
l2 = ttk.Label(win, text="Unit:", font=15)

# Meter radiobutton
rb1 = ttk.Radiobutton(win,text="m", variable=v, value='m')

# Feet radiobutton
rb2 = ttk.Radiobutton(win,text="ft", variable=v, value='ft')

# Depth label
l3 = ttk.Label(win, text = "Depth:", font=15)

# Depth entry
e = ttk.Entry(win, width=18)

# Rock types label
l4 = ttk.Label(win, text="Rock Type:", font=15)

# Rock types
c1 = ttk.Combobox(win, width=15, values = ["Sandstone: ", "Siltstone: ", "Chert: ",
                                 "Shale: ", "Claystone: ", "Marl: ",
                                 "Limestone: ", "Dolomite: ", "Chalk: ",
                                 "Anhydrite: ", "Gypsum: ", "Halite: ",
                                 "Coal: ", "Lignite: "])
# Combobox labels
l5 = ttk.Label(win, text = "colour:")
l6 = ttk.Label(win, text = "hardness:")
l7 = ttk.Label(win, text = "texture:")
l8 = ttk.Label(win, text = "grain size:")
l9 = ttk.Label(win, text = "sorting:")
l10 = ttk.Label(win, text = "angularity:")
l11 = ttk.Label(win, text = "sphericity:")
l12 = ttk.Label(win, text = "cement type:")
l13 = ttk.Label(win, text = "trace minerals:")
l14 = ttk.Label(win, text = "trace fossils:")

# Colours
c2 = ttk.Combobox(win, width=15, values = ['white', 'light grey', 'grey', 'dark grey',
                                           'purple', 'blue', 'light green', 'green',
                                           'pale yellow', 'yellow', 'pale orange', 'orange',
                                           'pale pink', 'pink', 'red', 'reddish brown',
                                           'moderate reddish brown', 'light brown',
                                           'greyish brown', 'moderate brown', 'brown',
                                           'dark brown', 'black'])
# Hardness
c3 = ttk.Combobox(win, width=15, values = ['unconsolidated', 'friable', 'soft', 'plastic',
                                           'firm', 'moderately hard', 'hard', 'very hard',
                                           'brittle', 'dense'])
# Texture
c4 = ttk.Combobox(win, width=15, values = ['blocky', 'sub-blocky', 'angular', 'conchoidal',
                                           'flaky', 'platy', 'fissile', 'splintery', 'amorphous',
                                           'homogeneous', 'heterogenous', 'sucrosic', 'vesicular',
                                           'earthy', 'smooth', 'etched frosted', 'pitted', 'striated'])
# Grain size
c5 = ttk.Combobox(win, width=15, values = ['ver fine', 'fine', 'medium', 'coarse', 'very coarse'])

# Sorting
c6 = ttk.Combobox(win, width=15, values = ['very poorly sorted', 'poorly sorted', 'moderately sorted',
                                           'well sorted', 'very well sorted'])
# Angularity
c7 = ttk.Combobox(win, width=15, values = ['angular', 'sub-angular', 'sub-rounded', 'rounded'])

# Spherocity
c8 = ttk.Combobox(win, width=15, values = ['elongate', 'sub-elongate', 'sub-spherical', 'spherical'])

# Cement
c9 = ttk.Combobox(win, width=15, values = ['calcareous', 'non-calcareous', 'dolomitic', 'silicious',
                                           'pyritic', 'hematitic', 'sideritic'])
# Trace minerals
c10 = ttk.Combobox(win, width=15, values = ['pyrite', 'claystone', 'siltstone', 'sandstone', 'calcite',
                                            'dolomite', 'siderite', 'K-feldspar','plagioclase',
                                            'glauconite', 'mica', 'chert'])
# Trace fossils
c11 = ttk.Combobox(win, width=15, values = ['gastropods', 'bivalves', 'foraminifera', 'ostracods',
                                            'diatoms', 'radiolaria', 'shell fragments', 'echinoids',
                                            'ammonites'])
# Action buttons
b3 = ttk.Button(win, text="PRINT")
b4 = ttk.Button(win, text="COPY")
b5 = ttk.Button(win, text="CLEAR")

# Text box
text = tkst.ScrolledText(win, wrap = tk.WORD, width=70, height=8)

##################
# Layout manager #
##################

l1.grid(row=0, column=0,columnspan=5, pady=20)

l2.grid(row=1, column=1, sticky = W, pady=10)

rb1.grid(row=1, column=2, sticky = W, pady=10)
rb2.grid(row=1, column=2, sticky = E, pady=10)

l3.grid(row=2, column=1, sticky = W, pady=10)
e.grid(row=2, column=2, sticky = W, pady=10)

l4.grid(row=3, column= 1, sticky = W, pady=10)
c1.grid(row=3, column=2, sticky = W, pady=10)

l5.grid(row=4, column=0, sticky = W, padx=5)
l6.grid(row=4, column=1, sticky = W, padx=5)
l7.grid(row=4, column=2, sticky = W, padx=5)
l8.grid(row=4, column=3, sticky = W, padx=5)
l9.grid(row=4, column=4, sticky = W, padx=5)

c2.grid(row=5, column=0, sticky = W, pady=5, padx=5)
c3.grid(row=5, column=1, sticky = W, pady=5, padx=5)
c4.grid(row=5, column=2, sticky = W, pady=10, padx=5)
c5.grid(row=5, column=3, sticky = W, pady=5, padx=5)
c6.grid(row=5, column=4, sticky = W, pady=5, padx=5)

l10.grid(row=6, column=0, sticky = W, padx=5)
l11.grid(row=6, column=1, sticky = W, padx=5)
l12.grid(row=6, column=2, sticky = W, padx=5)
l13.grid(row=6, column=3, sticky = W, padx=5)
l14.grid(row=6, column=4, sticky = W, padx=5)

c7.grid(row=7, column=0, sticky = W, pady=5, padx=5)
c8.grid(row=7, column=1, sticky = W, pady=5, padx=5)
c9.grid(row=7, column=2, sticky = W, pady=5, padx=5)
c10.grid(row=7, column=3, sticky = W, pady=5, padx=5)
c11.grid(row=7, column=4, sticky = W, pady=5, padx=5)

b3.grid(row=8, column=1, pady=10, padx=5)
b4.grid(row=8, column=2, pady=10, padx=5)
b5.grid(row=8, column=3, pady=10, padx=5)

text.grid(row=9, column=0, columnspan=10, pady=30, padx=5)

#############
# Functions #
#############

# Prints description
def printDescription():

    # Depth and unit (m or ft)    
    start_description = entry()+ c1.get() 

    # Rest of description
    raw_description= [c2.get(), c3.get(), c4.get(),
                      c5.get(), c6.get(), c7.get(), 
                      c8.get(), c9.get(), c10.get(),
                      c11.get()]
    
    # Creating a list with only selected options by the user
    description_list= [i for i in raw_description if i is not ""]

    # Joining selected options with a comma
    formated_description= ", ".join(description_list)

    # Joining depth and unit (if depth typed) with the rest of description
    final_description = start_description + formated_description

    # Inserting full description to the text box
    text.insert(tk.INSERT, final_description + '\n')

# Gets depth and units (if any chosen) for printDescription()
def entry():
    
    depth = str(e.get())
    if depth == "":
        return depth
    else:
        depth += ' ' + radioPrint() + " | "
        return depth

# Gets units chosen (m or ft) for entry()
def radioPrint():
    
    unit = v.get()
    return unit

# Copies content of textbox to clipboard
def copyToClipboard():
    
    win.clipboard_clear()
    win.clipboard_append(text.get(1.0, END))
    win.update() # now it stays on the clipboard after the window is closed

# Clears text box
def clearText():
    
    text.delete(1.0, END)
    
# Button command updates

b3["command"] = printDescription    
b4["command"] = copyToClipboard    
b5["command"] = clearText

############
# Mainloop #
############

win.mainloop()
