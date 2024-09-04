from tkinter import *
import db

class Window():
    def __init__(self, master=None) -> None:
        """initialize the application"""

        self.master = master
        self.master.title("Your Information")
        self.master.geometry("600x600+500+200")
        self.master.resizable(False, False)
        self.master.grid_columnconfigure(0, weight=1)

        self.build()
    
    
    def build(self) -> None:
        """call the building events"""

        self.config()
        self.frame()
        self.label()
        self.entry()
        self.button()

    
    def config(self) -> None:
        """pattern configuration"""

        self.title_font = ("Verdana", "18", "bold")
        self.text_font = ("Verdana", "12")

    
    def frame(self) -> None:
        """frame building"""

        self.logout_frame = Frame(self.master)
        self.logout_frame.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=10, sticky="nsew")
        self.logout_frame.grid_columnconfigure(0, weight=1)

        self.main_window = Frame(self.master)
        self.main_window.grid(row=1, column=0, columnspan=2, pady=(0, 50), padx=10, sticky="nsew")
        self.main_window.grid_columnconfigure(0, weight=1)

        self.name_frame = Frame(self.master)
        self.name_frame.grid(row=2, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="nsew")
        self.name_frame.grid_columnconfigure(0, weight=0)
        self.name_frame.grid_columnconfigure(1, weight=1)

        self.phone_frame = Frame(self.master)
        self.phone_frame.grid(row=3, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="nsew")
        self.phone_frame.grid_columnconfigure(0, weight=0)
        self.phone_frame.grid_columnconfigure(1, weight=1)

        self.email_frame = Frame(self.master)
        self.email_frame.grid(row=4, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="nsew")
        self.email_frame.grid_columnconfigure(0, weight=0)
        self.email_frame.grid_columnconfigure(1, weight=1)

        self.address_frame = Frame(self.master)
        self.address_frame.grid(row=5, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="nsew")
        self.address_frame.grid_columnconfigure(0, weight=0)
        self.address_frame.grid_columnconfigure(1, weight=1)

        self.password_frame = Frame(self.master)
        self.password_frame.grid(row=6, column=0, columnspan=2, pady=(20, 10), padx=10, sticky="nsew")
        self.password_frame.grid_columnconfigure(0, weight=0)
        self.password_frame.grid_columnconfigure(1, weight=1)

        self.action_frame = Frame(self.master)
        self.action_frame.grid(row=7, column=0, columnspan=2, pady=(30, 10), padx=10, sticky="nsew")
        self.action_frame.grid_columnconfigure(0, weight=0)
        self.action_frame.grid_columnconfigure(1, weight=1)
    
    
    def label(self) -> None:
        """label building"""

        self.hello_message = Label(self.main_window, text="Hello There!")
        self.hello_message.config(font=self.title_font)
        self.hello_message.grid(row=0, column=0, pady=(10, 0), padx=(10, 0), columnspan=2, sticky="n")

        self.name_label = Label(self.name_frame, text="Name:")
        self.name_label.config(font=self.text_font)
        self.name_label.grid(row=0, column=0, padx=(150,0), sticky="w")

        self.phone_label = Label(self.phone_frame, text="Phone:")
        self.phone_label.config(font=self.text_font)
        self.phone_label.grid(row=0, column=0, padx=(150,0), sticky="w")

        self.email_label = Label(self.email_frame, text="E-Mail:")
        self.email_label.config(font=self.text_font)
        self.email_label.grid(row=0, column=0, padx=(150,0), sticky="w")

        self.address_label = Label(self.address_frame, text="Address:")
        self.address_label.config(font=self.text_font)
        self.address_label.grid(row=0, column=0, padx=(150,0), sticky="w")

        self.password_label = Label(self.password_frame, text="Password:")
        self.password_label.config(font=self.text_font)
        self.password_label.grid(row=0, column=0, padx=(150,0), sticky="w")

    
    
    def entry(self) -> None:
        """entry building"""

        self.name_entry = Entry(self.name_frame)
        self.name_entry.grid(row=0, column=1, sticky="we", padx=(0,150))

        self.phone_entry = Entry(self.phone_frame)
        self.phone_entry.grid(row=0, column=1, sticky="we", padx=(0,150))

        self.email_entry = Entry(self.email_frame)
        self.email_entry.grid(row=0, column=1, sticky="we", padx=(0,150))

        self.address_entry = Entry(self.address_frame)
        self.address_entry.grid(row=0, column=1, sticky="we", padx=(0,150))

        self.password_entry = Entry(self.password_frame)
        self.password_entry.grid(row=0, column=1, sticky="we", padx=(0,150))
    
    
    def button(self) -> None:
        """button building"""

        self.logout_button = Button(self.logout_frame, text="Log out", command=self.logout, activebackground="gray", activeforeground="white")
        self.logout_button.grid(row=0, column=0, sticky="e", padx=10)

        self.delete_button = Button(self.action_frame, text="Delete Account", command=self.delete_account, activebackground="#d45c5c", activeforeground="white", width=25)
        self.delete_button.grid(row=0, column=0, sticky="we" ,padx=(100, 5))

        self.save_button = Button(self.action_frame, text="Save Changes", command=self.save_changes, activebackground="#b1cd71", width=25)
        self.save_button.grid(row=0, column=1, sticky="we" ,padx=(5, 100))

    
    def logout(self) -> None:
        self.master.destroy()

    
    def save_changes(self) -> None:
        print('hello')


    def delete_account(self) -> None:
        print('goodbye')


def main():
    root = Tk()
    Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
