from tkinter import *

class Window:
    def __init__(self, master=None) -> None:
        """initialize the application"""

        self.master = master
        self.build()

    def build(self) -> None:
        """call the building events"""

        self.config()
        self.frame()
        self.label()
        self.text()
    
    def config(self) -> None:
        """pattern configuration"""

        self.title_font = ("Verdana", "18", "bold")
        self.subtitle_font = ("Verdana", "15")
        self.text_font = ("Verdana", "12")
    
    def frame(self) -> None:
        """frame building"""

        self.main_window = Frame(self.master)
        self.main_window.pack()

        self.a = Frame(self.master)
        self.a.pack()
    
    def label(self) -> None:
        """label building"""

        self.title = Label(self.main_window, text="Welcome!")
        self.title["font"] = self.title_font
        self.title.pack()

        self.subtitle = Label(self.main_window, text="Please, Log in")
        self.subtitle["pady"] = 10
        self.subtitle["font"] = self.subtitle_font
        self.subtitle.pack()

        self.email_label = Label(self.main_window, text="E-mail:")
        self.email_label["pady"] = 20
        self.email_label["padx"] = 5
        self.email_label["font"] = self.text_font
        self.email_label.pack(side=LEFT)

        self.password_label = Label(self.a, text="Password:")
        self.password_label["padx"] = 5
        self.password_label["font"] = self.text_font
        self.password_label.pack(side=LEFT)
    
    def text(self) -> None:
        """text building"""

        self.email_text = Text(self.main_window, height=1, width=50)
        self.email_text.pack(side=LEFT)

        self.password_text = Entry(self.a)
        self.password_text.configure(show="*")
        self.password_text.pack(side=LEFT)



root = Tk()
root.title("")
root.geometry("600x600+400+200") #Because I want it here
root.resizable(True, True)
Window(root)
root.mainloop()