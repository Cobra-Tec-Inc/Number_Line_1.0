from tkinter import *
from tkinter import ttk
from time import *
from random import *


class Load(Tk):
    def __init__(self):
        super().__init__()

        self.width = 900
        self.height = 600
        self.bg = "#343949"

        self.geometry("900x600")
        self.title("Number Line 3.0")
        self.config(bg=self.bg)

        self.resizable(0, 0)
        self.iconbitmap(
            "Icon.ico")

        self.Draw()

    def Draw(self):

        self.image = PhotoImage(
            file="Icon.png")

        self.place = Label(
            self,
            image=self.image,
            bg=self.bg)
        self.place.place(x=self.width/3, y=self.height/6 - 50)

        self.Title = Label(
            self,
            text="Number Line",
            font=("Courier New", 20, "bold"),
            bg=self.bg,
            fg="#cccccc")
        self.Title.place(x=self.width/2.5, y=self.height/2 + 50)

        self.Comp = Label(
            self,
            text="Developed by Cobra Tec",
            font=("Courier New", 15, "bold"),
            bg=self.bg,
            fg="#cccccc")
        self.Comp.place(x=self.width/2.85, y=560)

        self.loading()

    def loading(self):

        self.progressbar = ttk.Progressbar(
            self, orient=HORIZONTAL, length=200, mode='determinate')
        self.progressbar.place(x=350, y=520)
        self.progressbar["maximum"] = 2

        for i in range(3):
            sleep(1)
            self.progressbar["value"] = i
            self.progressbar.update()
        self.kill()
        self.next()

    def kill(self):
        sleep(2)
        self.destroy()

    def next(self):
        main = Main()
        main.mainloop()


class Main(Tk):
    def __init__(self):
        super().__init__()

        self.bg = "#343949"

        self.geometry("900x600")
        self.title("Number Line 1.0")
        self.config(bg=self.bg)

        self.resizable(0, 0)
        self.iconbitmap("Icon.ico")

        self.Draw()
        self.Draw_Basic()

    def Draw(self):

        self.claculation = Entry(
            self,
            width=18,
            bg=self.bg,
            fg="white",
            font=("Courier New", 15, "bold"))
        self.claculation.place(x=450, y=10)

        self.typeArea = LabelFrame(
            self,
            width=175,
            height=900,
            bg=self.bg,
            fg="white")
        self.typeArea.place(x=0, y=0)

        self.basic = Button(
            self.typeArea,
            text="Basic",
            width=20,
            height=1,
            bg=self.bg,
            fg="white",
            font=("Courier New", 10, "bold"),
            command=self.Draw_Basic)
        self.basic.place(x=0, y=0)

        self.MoreComming = Label(
            self.typeArea,
            text="-More Comming-",
            width=20,
            height=1,
            bg=self.bg,
            fg="white",
            font=("Courier New", 10, "bold"))
        self.MoreComming.place(x=0, y=300)

        self.History = LabelFrame(
            self,
            width=175,
            height=900,
            font=("Courier New", 15, "bold"),
            bg=self.bg,
            fg="white")
        self.History.place(x=725, y=0)

        self.Hist_num = Label(
            self.History,
            text="",
            bg=self.bg,
            fg="white",
            font=("Courier New", 15, "bold"))
        self.Hist_num.place(x=0, y=40)

        self.label = Label(
            self.History,
            text="History",
            font=("Courier New", 15, "bold"),
            bg=self.bg,
            fg="white",
            padx=40)
        self.label.place(x=0, y=0)

        self.line = LabelFrame(
            self.History,
            width=175,
            height=2,
            font=("Courier New", 15, "bold"),
            bg=self.bg,
            fg="white")
        self.line.place(x=0, y=25)

    def Draw_Basic(self):

        self.three = Button(
            self,
            text="3",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('3'))
        self.three.place(x=570, y=250)

        self.two = Button(
            self,
            text="2",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('2'))
        self.two.place(x=510, y=250)

        self.one = Button(
            self,
            text="1",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('1'))
        self.one.place(x=450, y=250)

        self.six = Button(
            self,
            text="6",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('6'))
        self.six.place(x=570, y=190)

        self.five = Button(
            self,
            text="5",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('5'))
        self.five.place(x=510, y=190)

        self.four = Button(
            self,
            text="4",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('4'))
        self.four.place(x=450, y=190)

        self.nine = Button(
            self,
            text="9",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('9'))
        self.nine.place(x=570, y=130)

        self.eight = Button(
            self,
            text="8",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('8'))
        self.eight.place(x=510, y=130)

        self.seven = Button(
            self,
            text="7",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('7'))
        self.seven.place(x=450, y=130)

        self.equal = Button(
            self,
            text="=",
            bg="#252832",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            height=1,
            command=lambda: [self.click_But(
                "="), self.add_to_history(self.claculation.get())]
        )
        self.equal.place(x=630, y=310)

        self.zero = Button(
            self,
            text="0",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('0'))
        self.zero.place(x=510, y=310)

        self.C = Button(
            self,
            text="C",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But('C'))
        self.C.place(x=510, y=70)

        self.add = Button(
            self,
            text="+",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But("+"))
        self.add.place(x=630, y=250)

        self.sub = Button(
            self,
            text="-",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But("-"))
        self.sub.place(x=630, y=190)

        self.image = PhotoImage(
            file="Multi.png")

        self.mul = Button(
            self,
            text="*",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But("*"))
        self.mul.place(x=630, y=130)

        self.image = PhotoImage(
            file="Div.png")

        self.div = Button(
            self,
            text="/",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But("/"))
        self.div.place(x=630, y=70)

        self.point = Button(
            self,
            text=".",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.click_But("."))
        self.point.place(x=570, y=310)

        self.negative = Button(
            self,
            text="-/+",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=5,
            command=lambda: self.click_But("-"))
        self.negative.place(x=450, y=310)

    def add_to_history(self, hist):
        self.Hist_num["text"] = hist

    def click_But(self, key):

        # = -> calculate results
        if key == '=':
            # safeguard against integer division
            if '/' in self.claculation.get() and '.' not in self.claculation.get():
                self.claculation.insert(END, ".0")

            # attempt to evaluate results
            try:
                result = eval(self.claculation.get())
                self.claculation.insert(END, " = " + str(result))
            except:
                self.claculation.insert(END, "   Error, use only valid chars")

            # C -> clear display
        elif key == 'C':
            self.claculation.delete(0, END)
            # neg -> negate term
        elif key == 'neg':
            if '=' in self.claculation.get():
                self.claculation.delete(0, END)
            try:
                if self.claculation.get()[0] == '-':
                    self.claculation.delete(0)
                else:
                    self.claculation.insert(0, '-')
            except IndexError:
                pass

            # clear display and start new input
        else:
            if '=' in self.claculation.get():
                self.claculation.delete(0, END)
            self.claculation.insert(END, key)


"""
class functions():
    def __init__(self):
        super().__init__()

    def click_But(self, key):

        # = -> calculate results
        if key == '=':
            # safeguard against integer division
            if '/' in self.claculation.get() and '.' not in self.claculation.get():
                self.claculation.insert(END, ".0")

            # attempt to evaluate results
            try:
                result = eval(self.claculation.get())
                self.claculation.insert(END, " = " + str(result))
            except:
                self.claculation.insert(END, "   Error, use only valid chars")

            # C -> clear display
        elif key == 'C':
            self.claculation.delete(0, END)
            # neg -> negate term
        elif key == 'neg':
            if '=' in self.claculation.get():
                self.claculation.delete(0, END)
            try:
                if self.claculation.get()[0] == '-':
                    self.claculation.delete(0)
                else:
                    self.claculation.insert(0, '-')
            except IndexError:
                pass

            # clear display and start new input
        else:
            if '=' in self.claculation.get():
                self.claculation.delete(0, END)
            self.claculation.insert(END, key)
"""

if __name__ == "__main__":
    app = Load()
    app.mainloop()
