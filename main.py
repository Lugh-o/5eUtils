from tkinter import *
from DiceRoll import *

def validate_int(input_text):
    return input_text.isdigit() or (input_text and input_text[0] == '-' and input_text[1:].isdigit())

def diceRoll():
    amountValue = p1.amountEntry.get()
    sideValue = p1.sideEntry.get()
    resultValues.delete("1.0", END)
    
    try:
        amountValue = int(amountValue)
        sideValue = int(sideValue)
        result = roll(sideValue, amountValue)
        resultValues.insert(END, f"{result}\n")
    except ValueError:
        resultValues.insert(END, "Invalid input. Please enter valid numbers.\n")


class Page(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self):
        self.lift()

class DiceRoll(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        entryFrame = Frame(self)
        entryFrame.pack(pady=30, side='top')
        validate_cmd = (entryFrame.register(validate_int), '%P')

        self.sideLabel = Label(entryFrame, text="Number of Sides")
        self.sideLabel.grid(row=0, column=0, padx=5)
        self.sideEntry = Entry(entryFrame, bd=5, validate='key', validatecommand=validate_cmd)
        self.sideEntry.grid(row=0, column=1, padx=5)

        self.amountLabel = Label(entryFrame, text="Number of Dices")
        self.amountLabel.grid(row=1, column=0, padx=5)
        self.amountEntry = Entry(entryFrame, bd=5, validate='key', validatecommand=validate_cmd)
        self.amountEntry.grid(row=1, column=1, padx=5)

        Button(entryFrame, text="Roll", command=diceRoll).grid(row=2, column=0, columnspan=2)
        
        global resultValues
        resultValues = Text(self, height=10, width=40)
        resultValues.pack(pady=5)

class HitpointsCalculator(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global p1
        p1 = DiceRoll(self)
        p2 = HitpointsCalculator(self)

        buttonFrame = Frame(self)
        container = Frame(self)
        buttonFrame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonFrame, text="DiceRoll", command=p1.show)
        b2 = Button(buttonFrame, text="HitpointsCalculator", command=p2.show)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")

    root.mainloop()
