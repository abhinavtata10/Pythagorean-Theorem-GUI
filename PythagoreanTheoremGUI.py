import math
from tkinter import *

window = Tk()
window.geometry("800x500")
window.configure(bg="blue", padx=10, pady=10)
window.title("Pythagorean Theorem GUI")


def leg_label():
    s1Label.configure(text="a:")
    s2Label.configure(text="c:")
    resultLabel.configure(text="b = ___")

def hyp_label():
    s1Label.configure(text="a:")
    s2Label.configure(text="b:")
    resultLabel.configure(text="c = ___")

def calc():

    choice = float(lrb_hrb.get())
    if choice == 1:
        a = float(s1Entry.get())
        c = float(s2Entry.get())
        b = math.sqrt(c ** 2 - a ** 2)
        resultLabel.configure(text="b = " + str(b))
    elif choice == 2:
        a = float(s1Entry.get())
        b = float(s2Entry.get())
        c = math.hypot(a, b)
        resultLabel.configure(text="c = " + str(c))


rbFrame = Frame(window, bg="navy blue", padx=15, pady=15, width=400, height=400)
rbFrame.pack()
side1Frame = Frame(window, bg = "blue", padx=15, pady=15, width=400, height=400)
side1Frame.pack()
side2Frame = Frame(window, bg = "blue", padx=15, pady=15, width=400, height=400)
side2Frame.pack()
buttonFrame = Frame(window, bg = "blue", padx=15, pady=15, width=400, height=400)
buttonFrame.pack()

lrb_hrb = IntVar()

resultFrame = Frame(window, bg = "blue", padx=15, pady=15, width=400, height=400)
resultFrame.pack()
leg_rb = Radiobutton(rbFrame, bg="blue", fg="white", text="Calculate leg: ", font=("Courier", 25), value=1, variable =lrb_hrb, command=leg_label)
leg_rb.pack()
hyp_rb = Radiobutton(rbFrame, bg="blue", fg="white", text="Calculate hypotenuse: ", value=2, font=("Courier", 25), variable =lrb_hrb, command=hyp_label )
hyp_rb.pack()
s1Label = Label(side1Frame, bg="blue", fg="white", text="Enter: ", font=("Courier", 25))
s1Label.pack()
s1Entry = Entry(side1Frame, bg="white", fg="black", font=("Courier",25))
s1Entry.pack()
s2Label = Label(side2Frame, bg="blue", fg="white", text="Enter: ", font=("Courier", 25))
s2Label.pack()
s2Entry = Entry(side2Frame, bg="white", fg="black", font=("Courier",25))
s2Entry.pack()
calcButton = Button(buttonFrame, text ="Calculate", command= calc, height=2, width=12)
calcButton.pack()
resultLabel = Label(resultFrame, bg="navy blue", fg="white", text="_____", font=("Courier", 25))
resultLabel.pack()

window.mainloop()