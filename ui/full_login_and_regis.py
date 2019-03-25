import tkinter as tk
from tkinter import ttk
from classes import data
### this is the file where all the function and variable are join in this file.
from classes import user
from ui.after_login_succeed import fun_login_succeed

### These Classes are for the First Windows of the Program

global func_login_page


class Main_win(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ### Define Usefull Variables
        self.bar_color = "#2E2E2E"
        self.button_color = "#191516"
        self.heading_font = "Gautami 18 bold"
        self.norml_font = "Verdana 12 bold"
        self.entry_height = "Gautami 12"

        ### Create main main_container_win whre all the windows of program will be
        main_container_win = tk.Frame(self, relief="solid", bd="3")
        main_container_win.grid()
        main_container_win.grid_rowconfigure(0, weight=1)
        main_container_win.grid_columnconfigure(0, weight=1)

        ### Here is where all the program's windows are stored
        ### and first windows always will be StrtLoginPage
        self.frames = {}
        for F in (StrtLoginPage, RegisterPage, Available_tools):
            win_page_name = F.__name__
            frame = F(parent=main_container_win, controller=self)
            self.frames[win_page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StrtLoginPage")

    def show_frame(self, win_page_name):
        frame = self.frames[win_page_name]
        frame.tkraise()
        frame.postupdate()


class StrtLoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  StrtLoginPage frame setting
        self.controller = controller
        controller.grid_rowconfigure(0, weight=1)
        controller.grid_columnconfigure(0, weight=1)

        ### Code for StrtLoginPage
        welcome_head = tk.Label(self, text="Welcome to Share Power",
                                font=controller.heading_font,
                                bg=controller.bar_color,
                                fg="white",
                                height="0",
                                width="30").grid(row=0)

        ### Create variable if error comes while login set and show this varible with new string value
        error_message = tk.StringVar()
        error_message.set("Please Enter Username and Password")
        self.log_error_message = tk.Label(self, textvariable=error_message,
                                          font=controller.norml_font,
                                          bg=controller.bar_color,
                                          fg="white",
                                          bd=3,
                                          width="38")
        self.log_error_message.grid(row=1, column=0, columnspan=2)

        username_text = tk.Label(self, text="Usename",
                                 font=controller.norml_font,
                                 width="31", anchor="w", padx="39").grid(row=2, pady=(12, 2))
        self.username_entry = tk.Entry(self,
                                       font=controller.entry_height,
                                       width="34")
        self.username_entry.grid(row=3)

        password_text = tk.Label(self, text="Password",
                                 font=controller.norml_font,
                                 width="31", anchor="w", padx="39").grid(row=4, pady=(12, 2))
        self.password_entry = tk.Entry(self,
                                       font=controller.entry_height,
                                       width="34", show="*")
        self.password_entry.grid(row=5)

        welcome_head_bg = tk.Label(self,
                                   font="Gautami 15 bold",
                                   bg=controller.bar_color,
                                   height="0",
                                   width="31").grid(row=6, pady=(10, 2))
        ### Login_Function attache here
        login_button = tk.Button(self,
                                 text="Login",
                                 bd=2,
                                 font=controller.norml_font,
                                 padx=10,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 width="8",
                                 relief=tk.RIDGE, command=self.call_to_login_succed).grid(row=6, sticky="W", padx=45,
                                                                                          pady=(10, 2))

        or_label_text = tk.Label(self, text="Or", font=controller.norml_font).grid(row=7, sticky="nsew")

        ### Butoon to open Function of  Avalaible tools Window here
        Available_Tools_buton = tk.Button(self,
                                          text="See Available Tools",
                                          bd=2,
                                          font=controller.norml_font,
                                          padx=16,
                                          pady=10,
                                          bg=controller.button_color,
                                          fg="white",
                                          relief=tk.RIDGE, command=self.show_available_tools).grid(row=8, padx=40,
                                                                                                   pady=(0, 10),
                                                                                                   sticky="nsew")

        login_footer = tk.Label(self,
                                font=controller.heading_font,
                                bg=controller.bar_color,
                                height="0",
                                width="30").grid(row=9, pady=(20, 0))
        ### Button to move from login to Registeration
        login_button = tk.Button(self,
                                 text="Request Account",
                                 bd=2,
                                 font=controller.norml_font,
                                 padx=16,
                                 pady=1,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.login_page_to_regispage).grid(row=9, pady=(20, 0))
        ### This function load some thing after window is opened

    def show_available_tools(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.log_error_message.config(fg="white")
        self.controller.show_frame("Available_tools")

    def postupdate(self):
        self.username_entry.focus()

        ### This func will clear the Entry widget if there is any while chaging windows

    def login_page_to_regispage(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.log_error_message.config(fg="white")
        self.controller.show_frame("RegisterPage")

        ### This function is for to go inside of the program when user is verified

    def call_to_login_succed(self):
        data.current_user = user.user(str(self.username_entry.get()), str(self.password_entry.get()))
        if data.current_user.logged:
            self.controller.destroy()
            fun_login_succeed()
        else:
            self.log_error_message.config(fg="red")


### Here create class for RegisterPage
class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  RegisterPage frame setting
        self.controller = controller
        controller.grid_rowconfigure(0, weight=1)
        controller.grid_columnconfigure(0, weight=1)

        ### Code for RegisterPage
        reg_welcome_head = tk.Label(self, text="Register now to Share Power",
                                    font=controller.heading_font,
                                    bg=controller.bar_color,
                                    fg="white",
                                    height="0",
                                    width="30").grid(row=0, column=0, columnspan=2)

        ### Create variable if error comes set and show this varible with new string value
        self.error_message = tk.StringVar()
        self.error_message.set("Please fill all the given Fields")
        self.reg_error_message = tk.Label(self, textvariable=self.error_message,
                                          font=controller.norml_font,
                                          bg=controller.bar_color,
                                          fg="white",
                                          bd=3,
                                          width="38")
        self.reg_error_message.grid(row=1, column=0, columnspan=2)

        reg_fulname_text = tk.Label(self, text="Full Name :",
                                    font=controller.norml_font).grid(row=2, column=0, padx=(40, 0), pady=(20, 0))
        self.reg_fulname_entry = tk.Entry(self,
                                          font=controller.entry_height)
        self.reg_fulname_entry.grid(row=2, column=1, pady=(20, 0), padx=(0, 40))
        reg_username_text = tk.Label(self, text="Username :",
                                     font=controller.norml_font).grid(row=3, column=0, padx=(40, 0), pady=(20, 0))
        self.reg_username_entry = tk.Entry(self,
                                           font=controller.entry_height)
        self.reg_username_entry.grid(row=3, column=1, pady=(20, 0), padx=(0, 40))

        reg_password_text = tk.Label(self, text="Password :",
                                     font=controller.norml_font).grid(row=4, column=0, padx=(40, 0), pady=(20, 0))
        self.reg_password_entry = tk.Entry(self,
                                           font=controller.entry_height, show="*")
        self.reg_password_entry.grid(row=4, column=1, pady=(20, 0), padx=(0, 40))

        reg_bil_adres_text = tk.Label(self, text="Billing address :",
                                      font=controller.norml_font).grid(row=5, column=0, padx=(10, 0), pady=(20, 0))
        self.reg_bil_adres_entry = tk.Entry(self,
                                            font=controller.entry_height)
        self.reg_bil_adres_entry.grid(row=5, column=1, pady=(20, 0), padx=(0, 40))

        reg_email_text = tk.Label(self, text="Email address :",
                                  font=controller.norml_font).grid(row=6, column=0, padx=(10, 0), pady=(20, 0))
        self.reg_email_entry = tk.Entry(self,
                                        font=controller.entry_height)
        self.reg_email_entry.grid(row=6, column=1, pady=(20, 0), padx=(0, 40))

        regis_bg = tk.Label(self,
                            font="Gautami 15 bold",
                            bg=controller.bar_color,
                            height="0",
                            width="31").grid(row=7, column=0, columnspan=2, pady=(35, 2))
        ### Registration_Function attache here
        Registration_button = tk.Button(self,
                                        text="Sign Up",
                                        bd=2,
                                        font=controller.norml_font,
                                        padx=10,
                                        pady=0,
                                        bg=controller.button_color,
                                        fg="white",
                                        width="8",
                                        relief=tk.RIDGE, command=self.registration_command).grid(row=7, sticky="W",
                                                                                                 pady=(35, 2),
                                                                                                 padx=(46, 0))

        regis_footer = tk.Label(self,
                                font=controller.heading_font,
                                bg=controller.bar_color,
                                height="0",
                                width="30").grid(row=8, column=0, columnspan=2, pady=(48, 0), sticky="nsew")
        ### Button to move from Registeration to Login
        reg_to_login_button = tk.Button(self,
                                        text="Back to Login",
                                        bd=2,
                                        font=controller.norml_font,
                                        padx=16,
                                        pady=1,
                                        bg=controller.button_color,
                                        fg="white",
                                        relief=tk.RIDGE, command=self.regispage_page_to_login).grid(row=8, column=0,
                                                                                                    columnspan=2,
                                                                                                    pady=(48, 0))
        ### This function load some thing after window is opened

    def registration_command(self):
        fn = str(self.reg_fulname_entry.get())
        ba = str(self.reg_bil_adres_entry.get())
        pw = str(self.reg_password_entry.get())
        un = str(self.reg_username_entry.get())
        em = str(self.reg_email_entry.get())
        cond1 = self.validate_reg_detail(fn)
        cond2 = self.validate_reg_detail(ba)
        cond3 = self.validate_reg_detail(pw)
        cond4 = self.validate_reg_detail(un)
        cond5 = self.validate_reg_detail(em)
        cond_result = cond1 and cond2 and cond3 and cond4 and cond5
        if (cond_result):
            data.current_user = user.user(un, pw)
            status = data.current_user.register(em, fn, ba)
            if status:
                self.controller.destroy()
                fun_login_succeed()
            else:
                self.reg_error_message.config(fg="red")
                # self.reg_error_message.grid(row=1,column=0,columnspan=2)
        else:
            self.reg_error_message.config(fg="red")

    def validate_reg_detail(self, detail):
        if (len(detail) >= 4):
            return True
        else:
            return False

    def postupdate(self):
        self.reg_fulname_entry.focus()

        ### This func will clear the Entry widget if there is any while chaging windows

    def regispage_page_to_login(self):
        self.reg_fulname_entry.delete(0, "end")
        self.reg_username_entry.delete(0, "end")
        self.reg_password_entry.delete(0, "end")
        self.reg_bil_adres_entry.delete(0, "end")
        self.controller.show_frame("StrtLoginPage")
        self.reg_error_message.config(fg="white")


class Available_tools(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Available_tool_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)
        data.current_user = user.user("", "")
        self.bar_color = "#2E2E2E"
        self.button_color = "#191516"
        self.heading_font = "Gautami 19 bold"
        self.norml_font = "Verdana 12 bold"
        self.menu_buton_font = "Verdana 10 bold"
        self.entry_height = "Gautami 12"
        self.back_btn_fnt = "Verdana 11"
        self.sml_entry_height = "Gautami 9"
        self.bg_color = "#e6e6e6"

        ### Code for Available_tool_win
        tk.Label(self, font=self.menu_buton_font, width="105", bg=self.bar_color, height="3").grid(row=0,
                                                                                                   column=0,
                                                                                                   columnspan=7,
                                                                                                   sticky="nsew")
        tk.Label(self, font=self.menu_buton_font, bg=self.bg_color, height="10").grid(pady=(8, 0), padx=20,
                                                                                      row=1, column=0,
                                                                                      columnspan=7,
                                                                                      rowspan=5,
                                                                                      sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=self.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=self.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="This Is The List Of All Available Tools",
                 font=self.norml_font,
                 bg=self.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        ### Bring here User's Tools Data, the given below is just temporary data

        self.update()
        menu_bg_color = tk.Label(self, font=self.menu_buton_font, height="4", bg=self.bar_color).grid(
            pady=(18, 0), row=6, column=0, columnspan=7, sticky="nsew")

    def update(self):
        self.tree_col_heading2 = ("Tool Name", "Price", "Location", "Available Date")
        self.tree_data2 = []
        for x in data.current_user.available_tools:
            self.tree_data2.append([str(x.details['name']), str(x.details['price']), str(x.details['location']),
                                    str(x.details['available_due'])])
        '''self.tree_data2 = [
            ("Product 1", "Is 1000€", "London", "10/01/2019"),
            ("Product 2", "Is 400€", "Luton", "12/03/2019"),
            ("Product 3", "Is 2500€", "Luton", "20/06/2019"),
            ("Product 4", "Is 300€.", "Not Available", "13/02/2019")
        ]'''

        ### Setting font size of column heading etc.
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font="arial 12", rowheight=30)
        self.style.configure("mystyle.Treeview.Heading", font="arial 12 bold")

        self.tree2 = ttk.Treeview(self, style="mystyle.Treeview", columns=self.tree_col_heading2, show="headings")
        self.tree2.grid(column=0, columnspan=7, row=2, sticky='nsew', pady=(15, 5), padx="100")
        self.tree2.column(0, anchor=tk.S, width=2)
        self.tree2.column(1, anchor=tk.S, width=2)
        self.tree2.column(2, anchor=tk.S, width=2)
        self.tree2.column(3, anchor=tk.S, width=2)

        self.scrlbar2 = tk.Scrollbar(self, orient="vertical", command=self.tree2.yview)
        self.tree2.configure(yscrollcommand=self.scrlbar2.set)

        self.scrlbar2.grid(column=0, columnspan="7", row=2, sticky="ens", pady=(15, 5), padx="100")
        ### This loop is assignig value of heading from the varibale tree_col_heading2
        for col2 in self.tree_col_heading2:
            self.tree2.heading(col2, text=col2.title())

        ### This loop is assignig value of column and row from the varibale self.tree_data2
        for item2 in self.tree_data2:
            self.tree2.insert('', 'end', values=item2)

    def get_selected_value_from_treeview2(self):
        select_item2 = self.tree2.focus()
        selected_item2 = self.tree2.item(select_item2)
        print(selected_item2)
        self.tree2.selection_remove(self.tree2.focus())

    def postupdate(self):
        self.update()
        pass

    def goback_func(self):
        self.tree2.selection_remove(self.tree2.focus())
        self.controller.show_frame("StrtLoginPage")


### Execusiton of the all Windows

def func_login_page():
    MyApplication = Main_win()
    MyApplication.config(bg="#EAE9E9")
    MyApplication.resizable(False, False)
    MyApplication.geometry("960x540")
    data.current_user = user.user("", "")
    MyApplication.title("Sign in to Shared Power")
    MyApplication.mainloop()


if __name__ == "__main__":
    func_login_page()
