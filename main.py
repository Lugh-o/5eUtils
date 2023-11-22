from tkinter import *
from DiceRoll import *
from HitpointsCalculator import *

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

def CalculateHitpoints():
    global hasTough, isHillDwarf, useAverage, option
    hpResultField.delete("1.0", END)
    
    try:
        #[Wizard, Sorcerer, Artificer, Bard, Cleric, Druid, Monk, Rogue, Fighter, Paladin, Ranger, Barbarian]
        lvlAfterFirst = 12*[0]
        lvlAfterFirst[0] = int(p2.wizardLevel.get())
        lvlAfterFirst[1] = int(p2.sorcererLevel.get())
        lvlAfterFirst[2] = int(p2.artificerLevel.get())
        lvlAfterFirst[3] = int(p2.bardLevel.get())
        lvlAfterFirst[4] = int(p2.clericLevel.get())
        lvlAfterFirst[5] = int(p2.druidLevel.get())
        lvlAfterFirst[6] = int(p2.monkLevel.get())
        lvlAfterFirst[7] = int(p2.rogueLevel.get())
        lvlAfterFirst[8] = int(p2.fighterLevel.get())
        lvlAfterFirst[9] = int(p2.paladinLevel.get())
        lvlAfterFirst[10] =int(p2.rangerLevel.get())
        lvlAfterFirst[11] =int(p2.barbarianLevel.get())
        conModifier = int(p2.conMod.get())
        
        startingClass = option.get()
        
        match startingClass:
            case "Wizard" | "Sorcerer":
                startingDie = 6
            case "Artificer" | "Bard" | "Cleric" | "Druid" | "Monk" | "Rogue":
                startingDie = 8
            case "Fighter" | "Paladin" | "Ranger": 
                startingDie = 10
            case "Barbarian":
                startingDie = 12
    
                    
        hpResult = calcHP(startingDie, conModifier, lvlAfterFirst, hasTough.get(), isHillDwarf.get(), useAverage.get())
        hpResultField.insert(END, f"{hpResult}\n")
    except ValueError:
        hpResultField.insert(END, "Invalid input. Please enter valid numbers.\n")
        return 0

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
        self.sideEntry = Entry(entryFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.sideEntry.grid(row=0, column=1, padx=5)

        self.amountLabel = Label(entryFrame, text="Number of Dices")
        self.amountLabel.grid(row=1, column=0, padx=5)
        self.amountEntry = Entry(entryFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.amountEntry.grid(row=1, column=1, padx=5)

        Button(entryFrame, text="Roll", command=diceRoll).grid(row=2, column=0, columnspan=2)
        
        global resultValues
        resultValues = Text(self, height=10, width=40)
        resultValues.pack(pady=5)

class HitpointsCalculator(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        firstFrame = Frame(self)
        firstFrame.pack(pady=30, side='top')
        validate_cmd = (firstFrame.register(validate_int), '%P')    
        
        classes = ["Wizard", "Sorcerer", "Artificer", "Bard", 
                   "Cleric", "Druid", "Monk", "Rogue", 
                   "Fighter", "Paladin", "Ranger", "Barbarian"]        
        
        self.startingLabel = Label(firstFrame, text="Level 1 Class")
        self.startingLabel.grid(row=0, column=0, padx=5)
        
        global option
        option = StringVar()
        option.set(classes[0])
        self.startingClass = OptionMenu(firstFrame, option, *classes)
        self.startingClass.grid(row=0, column=1, padx=5)        
        
        self.conLabel = Label(firstFrame, text="Constitution Modifier")
        self.conLabel.grid(row=1, column=0, padx=5)
        self.conMod = Entry(firstFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.conMod.grid(row=1, column=1, padx=5)        
        self.conMod.insert(0, "0")
        
        afterFrame = Frame(self)
        afterFrame.pack(pady=30, side='top', anchor='center')
        
        validate_cmd = (afterFrame.register(validate_int), '%P')
        
        self.afterLabel = Label(afterFrame, text="Levels After the First")
        self.afterLabel.grid(row=1, column=3, padx=5, columnspan=2)
        
        self.wizardLabel = Label(afterFrame, text="Wizard")
        self.wizardLabel.grid(row=2, column=0, padx=5)
        self.wizardLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.wizardLevel.grid(row=2, column=1, padx=5)
        self.wizardLevel.insert(0, "0")
        
        self.sorcererLabel = Label(afterFrame, text="Sorcerer")
        self.sorcererLabel.grid(row=2, column=2, padx=5)
        self.sorcererLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.sorcererLevel.grid(row=2, column=3, padx=5)
        self.sorcererLevel.insert(0, "0")
        
        self.artificerLabel = Label(afterFrame, text="Artificer")
        self.artificerLabel.grid(row=2, column=4, padx=5)
        self.artificerLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.artificerLevel.grid(row=2, column=5, padx=5)
        self.artificerLevel.insert(0, "0")
        
        self.bardLabel = Label(afterFrame, text="Bard")
        self.bardLabel.grid(row=2, column=6, padx=5)
        self.bardLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.bardLevel.grid(row=2, column=7, padx=5)
        self.bardLevel.insert(0, "0")
        
        self.clericLabel = Label(afterFrame, text="Cleric")
        self.clericLabel.grid(row=3, column=0, padx=5)
        self.clericLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.clericLevel.grid(row=3, column=1, padx=5)
        self.clericLevel.insert(0, "0")
        
        self.druidLabel = Label(afterFrame, text="Druid")
        self.druidLabel.grid(row=3, column=2, padx=5)
        self.druidLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.druidLevel.grid(row=3, column=3, padx=5)        
        self.druidLevel.insert(0, "0")
        
        self.monkLabel = Label(afterFrame, text="Monk")
        self.monkLabel.grid(row=3, column=4, padx=5)
        self.monkLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.monkLevel.grid(row=3, column=5, padx=5)
        self.monkLevel.insert(0, "0")
        
        self.rogueLabel = Label(afterFrame, text="Rogue")
        self.rogueLabel.grid(row=3, column=6, padx=5)
        self.rogueLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.rogueLevel.grid(row=3, column=7, padx=5)        
        self.rogueLevel.insert(0, "0")
        
        self.fighterLabel = Label(afterFrame, text="Fighter")
        self.fighterLabel.grid(row=4, column=0, padx=5)
        self.fighterLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.fighterLevel.grid(row=4, column=1, padx=5)      
        self.fighterLevel.insert(0, "0")
         
        self.paladinLabel = Label(afterFrame, text="Paladin")
        self.paladinLabel.grid(row=4, column=2, padx=5)
        self.paladinLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.paladinLevel.grid(row=4, column=3, padx=5)      
        self.paladinLevel.insert(0, "0")
        
        self.rangerLabel = Label(afterFrame, text="Ranger")
        self.rangerLabel.grid(row=4, column=4, padx=5)
        self.rangerLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.rangerLevel.grid(row=4, column=5, padx=5)      
        self.rangerLevel.insert(0, "0")
                       
        self.barbarianLabel = Label(afterFrame, text="Barbarian")
        self.barbarianLabel.grid(row=4, column=6, padx=5)
        self.barbarianLevel = Entry(afterFrame, bd=5, width=2, validate='key', validatecommand=validate_cmd)
        self.barbarianLevel.grid(row=4, column=7, padx=5)   
        self.barbarianLevel.insert(0, "0")
        
        global hasTough, isHillDwarf, useAverage

        hasTough = BooleanVar()
        self.toughLabel = Label(afterFrame, text="Do you have the Tough feat?")
        self.toughLabel.grid(row=5, column=0, padx=5)
        Checkbutton(afterFrame, text='', variable= hasTough, onvalue=True, offvalue=False).grid(row=5, column=1)    
               
        isHillDwarf = BooleanVar()
        self.dwarfLabel = Label(afterFrame, text="Are you a Hill Dwarf?")
        self.dwarfLabel.grid(row=6, column=0, padx=5)
        Checkbutton(afterFrame, text='', variable= isHillDwarf, onvalue=True, offvalue=False).grid(row=6, column=1)    
        
        useAverage = BooleanVar()
        self.averageLabel = Label(afterFrame, text="Use Average Values Instead of Rolling Dice?")
        self.averageLabel.grid(row=7, column=0, padx=5)
        Checkbutton(afterFrame, text='', variable= useAverage, onvalue=True, offvalue=False).grid(row=7, column=1)    
        
        Button(afterFrame, text="Calculate", command=CalculateHitpoints).grid(row=8, column=3, columnspan=2)       
        
        global hpResultField
        hpResultField = Text(self, height=10, width=40)
        hpResultField.pack(pady=5)
         
                
class MainView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global p1, p2
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
