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
        self.title("Number Line 1.0")
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

        self.loading()

    def loading(self):

        self.progressbar = ttk.Progressbar(
            self, orient=HORIZONTAL, length=200, mode='determinate')
        self.progressbar.place(x=350, y=550)
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

        self.func = functions()

        self.Draw()
        self.Draw_Basic()

    def Draw(self):

        self.claculation = Entry(
            self,
            width=18,
            bg=self.bg,
            fg="white",
            font=("Courier New", 15, "bold"),
            textvariable=self.func.equation)
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
            command=lambda: self.func.click_btn(3))
        self.three.place(x=570, y=250)

        self.two = Button(
            self,
            text="2",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(2))
        self.two.place(x=510, y=250)

        self.one = Button(
            self,
            text="1",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(1))
        self.one.place(x=450, y=250)

        self.six = Button(
            self,
            text="6",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(6))
        self.six.place(x=570, y=190)

        self.five = Button(
            self,
            text="5",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(5))
        self.five.place(x=510, y=190)

        self.four = Button(
            self,
            text="4",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(4))
        self.four.place(x=450, y=190)

        self.nine = Button(
            self,
            text="9",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(9))
        self.nine.place(x=570, y=130)

        self.eight = Button(
            self,
            text="8",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(8))
        self.eight.place(x=510, y=130)

        self.seven = Button(
            self,
            text="7",
            bg=self.bg,
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn(7))
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
            command=lambda: [self.func.equal_btn(), self.add_to_history()]
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
            command=lambda: self.func.click_btn(0))
        self.zero.place(x=510, y=310)

        self.C = Button(
            self,
            text="C",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=self.func.clr_btn)
        self.C.place(x=510, y=70)

        self.add = Button(
            self,
            text="+",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn("+"))
        self.add.place(x=630, y=250)

        self.sub = Button(
            self,
            text="-",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn("-"))
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
            command=lambda: self.func.click_btn("*"))
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
            command=lambda: self.func.click_btn("/"))
        self.div.place(x=630, y=70)

        self.point = Button(
            self,
            text=".",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=15,
            command=lambda: self.func.click_btn("."))
        self.point.place(x=570, y=310)

        self.negative = Button(
            self,
            text="-/+",
            bg="#414658",
            fg="white",
            font=("Courier New", 12, "bold"),
            pady=10,
            padx=5,
            command=lambda: self.func.click_btn("-"))
        self.negative.place(x=450, y=310)

    def add_to_history(self):
        self.Hist_num["text"] = self.claculation.get()


class functions():
    def __init__(self):
        super().__init__()

        self.operator = ''
        self.equation = StringVar()

    def click_btn(self, number):
        global operator
        self.operator = self.operator + str(number)
        self.equation.set(self.operator)

    def equal_btn(self):
        global operator
        self.add = str(eval(self.operator))
        self.equation.set(self.add)
        self.operator = ''

    def equal_btn(self):
        global operator
        self.sub = str(eval(self.operator))
        self.equation.set(self.sub)
        self.operator = ''

    def equal_btn(self):
        global operator
        self.div = str(eval(self.operator))
        self.equation.set(self.div)
        self.operator = ''

    def equal_btn(self):
        global operator
        self.mult = str(eval(self.operator))
        self.equation.set(self.mult)
        self.operator = ''

    def clr_btn(self):
        self.equation.set('')


if __name__ == "__main__":
    app = Load()
    app.mainloop()
