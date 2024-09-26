from tkinter import *
import db

class Window():
    def __init__(self, master, name_param, email, password) -> None:
        """initialize the application"""

        self.master = master
        self.master.title('Your Information')
        self.master.geometry('600x600+500+200')
        self.master.resizable(False, False)
        self.master.grid_columnconfigure(0, weight=1)

        self.name_param = name_param

        self.build()
        if name_param == 'login':
            self.retrieve_user_data(email, password)
    
    
    def build(self) -> None:
        """call the building events"""

        self.config()
        self.frame()
        self.label()
        self.entry()
        self.button()

    
    def config(self) -> None:
        """pattern configuration"""

        self.title_font = ('Verdana', '18', 'bold')
        self.text_font = ('Verdana', '12')
        self.message_font = ('Verdana', '8', 'bold')
        self.validate_digit = (self.master.register(self.only_numbers), '%S')

    
    def frame(self) -> None:
        """frame building"""

        self.logout_frame = Frame(self.master)
        self.logout_frame.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=10, sticky='nsew')
        self.logout_frame.grid_columnconfigure(0, weight=1)

        self.main_window = Frame(self.master)
        self.main_window.grid(row=1, column=0, columnspan=2, pady=(0, 20), padx=10, sticky='nsew')
        self.main_window.grid_columnconfigure(0, weight=1)

        self.id_frame = Frame(self.master)
        self.id_frame.grid(row=2, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.id_frame.grid_columnconfigure(0, weight=0)

        self.name_frame = Frame(self.master)
        self.name_frame.grid(row=3, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.name_frame.grid_columnconfigure(0, weight=0)
        self.name_frame.grid_columnconfigure(1, weight=1)

        self.phone_frame = Frame(self.master)
        self.phone_frame.grid(row=4, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.phone_frame.grid_columnconfigure(0, weight=0)
        self.phone_frame.grid_columnconfigure(1, weight=1)

        self.email_frame = Frame(self.master)
        self.email_frame.grid(row=5, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.email_frame.grid_columnconfigure(0, weight=0)
        self.email_frame.grid_columnconfigure(1, weight=1)

        self.address_frame = Frame(self.master)
        self.address_frame.grid(row=6, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.address_frame.grid_columnconfigure(0, weight=0)
        self.address_frame.grid_columnconfigure(1, weight=1)

        self.password_frame = Frame(self.master)
        self.password_frame.grid(row=7, column=0, columnspan=2, pady=(20, 10), padx=10, sticky='nsew')
        self.password_frame.grid_columnconfigure(0, weight=0)
        self.password_frame.grid_columnconfigure(1, weight=1)

        self.message_frame = Frame(self.master)
        self.message_frame.grid(row=8, column=0, columnspan=2, pady=(0, 5), padx=10, sticky='nsew')
        self.message_frame.grid_columnconfigure(0, weight=0)
        self.message_frame.grid_columnconfigure(1, weight=1)

        self.action_frame = Frame(self.master)
        self.action_frame.grid(row=9, column=0, columnspan=2, pady=(0, 10), padx=10, sticky='nsew')
        self.action_frame.grid_columnconfigure(0, weight=0)
        self.action_frame.grid_columnconfigure(1, weight=1)
    
    
    def label(self) -> None:
        """label building"""

        self.hello_message = Label(self.main_window, text='Hello There!')
        self.hello_message.config(font=self.title_font)
        self.hello_message.grid(row=0, column=0, pady=(10, 0), padx=(10, 0), columnspan=2, sticky='n')

        self.name_label = Label(self.name_frame, text='Name:')
        self.name_label.config(font=self.text_font)
        self.name_label.grid(row=0, column=0, padx=(150,0), sticky='w')

        self.phone_label = Label(self.phone_frame, text='Phone:')
        self.phone_label.config(font=self.text_font)
        self.phone_label.grid(row=0, column=0, padx=(150,0), sticky='w')

        self.email_label = Label(self.email_frame, text='E-Mail:')
        self.email_label.config(font=self.text_font)
        self.email_label.grid(row=0, column=0, padx=(150,0), sticky='w')

        self.address_label = Label(self.address_frame, text='Address:')
        self.address_label.config(font=self.text_font)
        self.address_label.grid(row=0, column=0, padx=(150,0), sticky='w')

        self.password_label = Label(self.password_frame, text='Password:')
        self.password_label.config(font=self.text_font)
        self.password_label.grid(row=0, column=0, padx=(150,0), sticky='w')

        self.message_label = Label(self.message_frame, fg='orange', wraplength=500)
        self.message_label.config(font=self.message_font)
        self.message_label.grid(row=0, column=0, pady=(0, 10), padx=(10, 0), columnspan=2, sticky='n')

    
    
    def entry(self) -> None:
        """entry building"""

        self.id_entry = Entry(self.id_frame)
        if self.name_param == 'register':
            self.id_entry.config(state='disabled')
        self.id_entry.grid(row=0, column=1, sticky='e', padx=(150,0))

        self.name_entry = Entry(self.name_frame)
        self.name_entry.grid(row=0, column=1, sticky='we', padx=(0,150))
        self.name_entry.focus_set()

        self.phone_entry = Entry(self.phone_frame, validate='key', validatecommand=self.validate_digit)
        self.phone_entry.grid(row=0, column=1, sticky='we', padx=(0,150))

        self.email_entry = Entry(self.email_frame)
        self.email_entry.grid(row=0, column=1, sticky='we', padx=(0,150))

        self.address_entry = Entry(self.address_frame)
        self.address_entry.grid(row=0, column=1, sticky='we', padx=(0,150))

        self.password_entry = Entry(self.password_frame)
        self.password_entry.grid(row=0, column=1, sticky='we', padx=(0,150))
    
    
    def button(self) -> None:
        """button building"""

        if self.name_param == 'login':
            self.logout_button = Button(self.logout_frame, text='Log out', command=self.logout, activebackground='gray', activeforeground='white')
        else:
            self.logout_button = Button(self.logout_frame, text='Quit', command=self.logout, activebackground='gray', activeforeground='white')
        self.logout_button.grid(row=0, column=0, sticky='e', padx=10)

        if self.name_param == 'login':
            self.delete_button = Button(self.action_frame, text='Delete Account', command=self.delete_account, activebackground='#d45c5c', activeforeground='white', width=25)
            self.delete_button.grid(row=0, column=0, sticky='we' ,padx=(100, 5))

        self.save_button = Button(self.action_frame, text='Save Changes', command=self.save_changes, activebackground='#b1cd71', width=25)
        self.save_button.grid(row=0, column=1, sticky='e' ,padx=(5, 100))

    
    def logout(self) -> None:
        self.master.destroy()

    
    def save_changes(self) -> None:
        """create user if register else update"""

        if self.email_verification():
            user_data = {
                'id':self.id_entry.get(),
                'name':self.name_entry.get(),
                'phone':self.phone_entry.get(),
                'email':self.email_entry.get(),
                'address':self.address_entry.get(),
                'password':self.password_entry.get()
            }

            error = self.verify_blank_fields(user_data)
            if error == None:
                if self.name_param == 'register':
                    self.message_label.config(text=db.create_user(user_data=user_data))
                elif self.name_param == 'login':
                    self.message_label.config(text=db.update_user(user_data=user_data))
                else:
                    self.message_label.config(text=user_data)
            else:
                self.message_label.config(text=error)
    

    def email_verification(self) -> False:
        """verify email existance"""

        if self.name_param == 'register':
            error = db.verify_email_existance(self.email_entry.get())
            self.message_label.config(text=error)
            return False if error != None else True
        elif self.name_param == 'login':
            error = None
            email = db.return_id_email(self.id_entry.get())[0]
            if email != self.email_entry.get():
                error = 'E-mail already exists!'
                self.message_label.config(text=error)
            return False if error != None else True


    def delete_account(self) -> None:
        """delete user if login"""

        if self.name_param == 'login':
            error = db.delete_user(self.id_entry.get())
            self.message_label.config(text=error)
            if error == 'Success!':
                self.master.destroy()



    def retrieve_user_data(self, email:str, password:str) -> None:
        """select in database based on email and password"""

        if self.name_param == 'login':
            self.user_data = db.user_data(email, password)

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, self.user_data['user_name'])

            self.phone_entry.delete(0, END)
            self.phone_entry.insert(0, self.user_data['user_phone'])

            self.email_entry.delete(0, END)
            self.email_entry.insert(0, self.user_data['user_email'])

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, self.user_data['user_address'])

            self.id_entry.delete(0, END)
            self.id_entry.insert(0, self.user_data['user_id'])
            self.id_entry.config(state='disabled')

            self.password_entry.delete(0, END)
            self.password_entry.insert(0, self.user_data['user_password'])



    def verify_blank_fields(self, user_data:dict) -> None:
        """checks for any empty fields"""

        if all(value and value.strip() != '' for key, value in user_data.items() if key != 'id'):
            return None
        else:
            return 'Please, fill the field(s): ' + ', '.join(key for key, value in user_data.items() if value.strip() == '' and key != 'id')


    def only_numbers(self, char:str) -> None:
        """validates if is a number"""

        return char.isdigit()
    

def main():
    root = Tk()
    Window(root, 'main', '', '')
    root.mainloop()


if __name__ == '__main__':
    main()
