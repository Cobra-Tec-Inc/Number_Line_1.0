from tkinter import *
from tkinter import ttk
from time import *
from tkinter.ttk import Combobox


class Load(Tk):
    def __init__(self):
        super().__init__()

        self.width = 400
        self.height = 400
        self.bg = "#363636"

        self.geometry("400x400")
        self.title("Time Line 2.0")
        self.config(bg=self.bg)

        self.resizable(0, 0)
        self.iconbitmap(
            "Icon_1.ico")

        self.Draw()

    def Draw(self):

        self.image = PhotoImage(
            file="Icon.png",)

        self.place = Label(
            self,
            image=self.image,
            bg=self.bg
        )
        self.place.place(x=self.width/2.3, y=self.height/5)

        self.Title = Label(
            self,
            text="Time Line",
            font=("Courier New", 20, "bold"),
            bg=self.bg,
            fg="#cccccc")
        self.Title.place(x=self.width/3, y=self.height/1.8)

        self.Comp = Label(
            self,
            text="Developed by Cobra Tec",
            font=("Courier New", 15, "bold"),
            bg=self.bg,
            fg="#cccccc")
        self.Comp.place(x=self.width/5.2, y=360)

        self.loading()

    def loading(self):

        self.progressbar = ttk.Progressbar(
            self, orient=HORIZONTAL, length=200, mode='determinate')
        self.progressbar.place(x=110, y=320)
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

        self.geometry("400x400")
        self.title("Time Line 1.0")
        self.config(bg="#363636")

        self.resizable(0, 0)
        self.iconbitmap(
            "Icon_1.ico")

        self.draw_Clock()
        self.run_clock()
        self.run_AM_PM()
        self.run_date()

    def draw_Clock(self):

        self.date = Label(
            self,
            font=("Digital-7", 30, "bold"),
            bg="#363636",
            fg="white"
        )
        self.date.place(x=110, y=40)

        self.clock = Label(
            self,
            font=("Digital-7", 70, "bold"),
            bg="#363636",
            fg="white"
        )
        self.clock.place(x=70, y=150)

        self.pm = Label(
            self,
            text="%p",
            font=("Digital-7", 20, "bold"),
            bg="#363636",
            fg="white"
        )
        self.pm.place(x=190, y=350)

    def run_clock(self):
        self.time = strftime("%H:%M:%S")

        self.clock.config(text=self.time)
        self.clock.after(200, self.run_clock)

    def run_date(self):
        self.d = strftime("%d/%m/%Y")

        self.date.config(text=self.d)
        self.date.after(200, self.run_clock)

    def run_AM_PM(self):
        self.pa = strftime("%p")
        self.pm.config(text=self.pa)
        self.pm.after(200, self.run_AM_PM)


if __name__ == "__main__":
    app = Load()
    app.mainloop()
