from tkinter import *
import data
import db

class Window:
    def __init__(self, master=None) -> None:
        """initialize the application"""

        self.master = master
        self.master.grid_columnconfigure(0, weight=1)
        self.build()

    
    def build(self) -> None:
        """call the building events"""

        self.config()
        self.frame()
        self.label()
        self.entry()
        self.button()
        db.create_table()
        db.select()
    
    
    def config(self) -> None:
        """pattern configuration"""

        self.title_font = ('Verdana', '18', 'bold')
        self.subtitle_font = ('Verdana', '15')
        self.text_font = ('Verdana', '12')
        self.message_font = ('Verdana', '8', 'bold')
    
    
    def frame(self) -> None:
        """frame building"""

        self.main_window = Frame(self.master)
        self.main_window.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.main_window.grid_columnconfigure(0, weight=1)

        self.email_frame = Frame(self.master)
        self.email_frame.grid(row=1, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.email_frame.grid_columnconfigure(0, weight=0)
        self.email_frame.grid_columnconfigure(1, weight=1)

        self.password_frame = Frame(self.master)
        self.password_frame.grid(row=2, column=0, columnspan=2, pady=(10, 20), padx=10, sticky='nsew')
        self.password_frame.grid_columnconfigure(0, weight=0)
        self.password_frame.grid_columnconfigure(1, weight=1)

        self.message_frame = Frame(self.master)
        self.message_frame.grid(row=3, column=0, columnspan=2, pady=(0, 5), padx=10, sticky='nsew')
        self.message_frame.grid_columnconfigure(0, weight=0)
        self.message_frame.grid_columnconfigure(1, weight=1)

        self.action_frame = Frame(self.master)
        self.action_frame.grid(row=4, column=0, columnspan=2, pady=(10, 20), padx=10, sticky='nsew')
        self.action_frame.grid_columnconfigure(0, weight=0)
        self.action_frame.grid_columnconfigure(1, weight=1)
    
    
    def label(self) -> None:
        """label building"""

        self.title = Label(self.main_window, text='Welcome!')
        self.title['font'] = self.title_font
        self.title.grid(row=0, column=0, pady=(10, 0), padx=(10, 0), columnspan=2, sticky='n')

        self.subtitle = Label(self.main_window, text='Please, Log in')
        self.subtitle['font'] = self.subtitle_font
        self.subtitle.grid(row=1, column=0, pady=(10, 20), padx=(10, 0), columnspan=2, sticky='n')

        self.email_label = Label(self.email_frame, text='E-mail:')
        self.email_label['font'] = self.text_font
        self.email_label.grid(row=0, column=0, padx=(100,0), sticky='w')

        self.password_label = Label(self.password_frame, text='Password:')
        self.password_label['font'] = self.text_font
        self.password_label.grid(row=0, column=0, padx=(100,0), sticky='w')

        self.message_label = Label(self.message_frame, fg='orange', wraplength=500)
        self.message_label.config(font=self.message_font)
        self.message_label.grid(row=0, column=0, pady=(0, 10), padx=(10, 0), columnspan=2, sticky='n')
    
    
    def entry(self) -> None:
        """entry building"""

        self.email_text = Entry(self.email_frame)
        self.email_text.grid(row=0, column=1, sticky='we', padx=(5, 100))
        self.email_text.focus_set()

        self.password_text = Entry(self.password_frame)
        self.password_text.configure(show='*')
        self.password_text.grid(row=0, column=1, sticky='we', padx=(5, 100))

   
    def button(self) -> None:
        """button building"""

        self.login = Button(self.action_frame, text='Log In', command=self.actionLogIn, width=25, activebackground='gray', activeforeground='white')
        self.login.grid(row=0, column=0, padx=(100, 5))

        self.register = Button(self.action_frame, text='Register', command=self.registerIn, width=25, activebackground='gray', activeforeground='white')
        self.register.grid(row=0, column=1, padx=(5,100))

    
    def actionLogIn(self) -> None:
        """does login"""

        error = db.check_login_and_password(self.email_text.get(), self.password_text.get())
        if error == 'login':
            self.data_window = Toplevel(self.master)
            self.data_app = data.Window(self.data_window, error, self.email_text.get(), self.password_text.get())
        else:
            self.message_label.config(text=error)

    
    def registerIn(self) -> None:
        """register user"""

        self.data_window = Toplevel(self.master)
        self.data_app = data.Window(self.data_window, 'register', '', '')


def main():
    root = Tk()
    root.title('System Login')
    root.geometry('600x600+400+200')
    root.resizable(False, False)
    Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
