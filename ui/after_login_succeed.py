from tkinter import messagebox
import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

from classes import data
from classes import tool


### this is the file where all the function and variable are join in this file.


### These Classes are for When User is login these window will open


class Login_Succeed(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ### Define Usefull Variables
        self.bar_color = "#2E2E2E"
        self.button_color = "#191516"
        self.heading_font = "Gautami 19 bold"
        self.norml_font = "Verdana 12 bold"
        self.menu_buton_font = "Verdana 10 bold"
        self.entry_height = "Gautami 12"
        self.back_btn_fnt = "Verdana 11"
        self.sml_entry_height = "Gautami 9"
        self.bg_color = "#e6e6e6"

        ### Create container_win whre all the windows of program will be
        container_win = tk.Frame(self, relief="solid", bd="2")
        container_win.grid()

        ### Here is where all the program's windows are stored
        ### and first windows always will be Login_succed_main_page
        self.frames = {}
        for F in (Login_succed_main_page, Available_tool_win,
                  Offered_tool_win, Hired_tool_win, Edit_profile_win, Offer_new_tool_win, Invoces_window,
                  Specific_tool_detail_win, Return_requested_window):
            page_name = F.__name__
            frame = F(parent=container_win, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login_succed_main_page")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.postupdate()
        data.reload()


class Login_succed_main_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ###  Login_succed_main_page frame setting
        self.controller = controller

        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(1, weight=1)

        ### Code for Login_succed_main_page
        ### All the Buttons for other pages go here
        menu_button1 = tk.Button(self, text="Edit Profile",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.main_page_to_Edit_profile_win)
        menu_button1.grid(row=0, column=0, sticky="nsew")
        menu_button2 = tk.Button(self, text="Invoices",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.main_page_to_Invoces_window)
        menu_button2.grid(row=0, column=1, sticky="nsew")
        menu_button3 = tk.Button(self, text="Hired Tools",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.main_page_to_Hired_tool_win)
        menu_button3.grid(row=0, column=2, sticky="nsew")
        menu_button4 = tk.Button(self, text="Offer New Tool",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.main_page_to_Offer_new_tool_win)
        menu_button4.grid(row=0, column=3, sticky="nsew")
        menu_button5 = tk.Button(self, text="Offered Tools",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.main_page_to_Offered_tool_win)
        menu_button5.grid(row=0, column=4, sticky="nsew")
        menu_button6 = tk.Button(self, text="Available Tools",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.main_page_to_Available_tool_win)
        menu_button6.grid(row=0, column=5, sticky="nsew")

        menu_button7 = tk.Button(self, text="Sign Out",
                                 bd=0,
                                 font=controller.menu_buton_font,
                                 padx=20,
                                 pady=6,
                                 bg=controller.bar_color,
                                 fg="white",
                                 relief=tk.FLAT, command=self.signout_func)
        menu_button7.grid(row=0, column=6, sticky="e")

        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, width="105", height="1").grid(row=1, column=0,
                                                                                                      columnspan=7,
                                                                                                      sticky="nsew")

        ### Image for the Logo
        self.logoImage = tk.PhotoImage(file="ui/logo.png")
        logo_img = tk.Label(self, image=self.logoImage).grid(row=2, column=0, columnspan=7, sticky="nsew")

        ### Veriable to get the Username and then this will print to the main screen
        self.welcome_user_mesg = tk.StringVar()
        self.welcome_user_mesg.set("Welcome User to Shared Power")
        welcome_user_tag = tk.Label(self, textvariable=self.welcome_user_mesg, font=controller.norml_font)
        welcome_user_tag.grid(row=3, column=0, columnspan=7, pady=(0, 5), sticky="nsew")

        self.serch_entry = tk.Entry(self, font=controller.entry_height,
                                    width="30")
        self.serch_entry.grid(row=5, column=0, columnspan=7)

        ### Search button function
        search_butn = tk.Button(self,
                                text="Search Now",
                                bd=2,
                                font=controller.norml_font,
                                padx=15,
                                pady=3,
                                bg=controller.button_color,
                                fg="white",
                                width="8",
                                relief=tk.RIDGE, command="")  # TODO do nothing at the current moment
        search_butn.grid(row=7, column=0, columnspan=7, pady=(10, 76))

        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(row=9,
                                                                                                                  column=0,
                                                                                                                  columnspan=7,
                                                                                                                  sticky="nsew")

        ### This function load some thing after window is opened

    def postupdate(self):
        self.serch_entry.focus()

        ### This function is for signout it will take you to the login_page

    def signout_func(self):
        MsgBox = messagebox.askquestion('Exit Shared Power', 'Are you sure you want to exit from Application')
        if MsgBox == "yes":
            self.controller.destroy()
            exit(0)

    def main_page_to_Offer_new_tool_win(self):
        self.serch_entry.delete(0, "end")
        self.controller.show_frame("Offer_new_tool_win")

    def main_page_to_Edit_profile_win(self):
        self.serch_entry.delete(0, "end")
        self.controller.show_frame("Edit_profile_win")

    def main_page_to_Invoces_window(self):
        self.serch_entry.delete(0, "end")
        self.controller.show_frame("Invoces_window")

    def main_page_to_Hired_tool_win(self):
        self.serch_entry.delete(0, "end")
        self.controller.show_frame("Hired_tool_win")

    def main_page_to_Offered_tool_win(self):
        self.serch_entry.delete(0, "end")
        self.controller.show_frame("Offered_tool_win")

    def main_page_to_Available_tool_win(self):
        self.serch_entry.delete(0, "end")
        self.controller.show_frame("Available_tool_win")


### Here create class for Offer_new_tool_win
class Offer_new_tool_win(tk.Frame):

    def __init__(self, parent, controller):
        self.img_filename = None
        tk.Frame.__init__(self, parent)
        ###  Offer_new_tool_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)

        ### Code for Offer_new_tool_win
        menu_bg_colors = tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color,
                                  height="3").grid(row=0, column=0, columnspan=7, sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(16, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=8,
                                                                                                  sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        self.error = tk.Label(self, text="Please Enter Fields To Upload Your Tool",
                              font=controller.norml_font,
                              bg=controller.bar_color,
                              fg="white"
                              )
        self.error.grid(row=0, column=0, columnspan=7)

        tk.Label(self, text="Product Name* :",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=1, column=0, pady=(40, 2), padx=(0, 20), sticky="e")

        self.Product_Name_entry = tk.Entry(self,
                                           font=controller.sml_entry_height,
                                           width="25")
        self.Product_Name_entry.grid(row=1, column=1, pady=(40, 2), sticky="w")

        tk.Label(self, text="Delivery Cost :",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=2, column=0, pady=(30, 2), padx=(0, 20), sticky="e")

        self.Delivery_Cost_entry = tk.Entry(self,
                                            font=controller.sml_entry_height,
                                            width="25")
        self.Delivery_Cost_entry.grid(row=2, column=1, pady=(30, 2), sticky="w")

        tk.Label(self, text="Available Date YYYY-MM-DD:",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=3, column=0, pady=(30, 2), padx=(0, 20), sticky="e")

        self.Available_Date_entry = tk.Entry(self,
                                             font=controller.sml_entry_height,
                                             width="25")
        self.Available_Date_entry.grid(row=3, column=1, pady=(30, 2), sticky="w")

        tk.Label(self, text="Product Price* :",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=4, column=0, pady=(30, 2), padx=(0, 20), sticky="e")

        self.Product_Price_entry = tk.Entry(self,
                                            font=controller.sml_entry_height,
                                            width="25")
        self.Product_Price_entry.grid(row=4, column=1, pady=(30, 2), sticky="w")

        tk.Label(self, text="Location* :",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=5, column=0, pady=(30, 2), padx=(0, 20), sticky="e")

        self.Location_entry = tk.Entry(self,
                                       font=controller.sml_entry_height,
                                       width="25")
        self.Location_entry.grid(row=5, column=1, pady=(30, 2), sticky="w")

        ### Upload tool Button, function is attache here
        tk.Button(self, text="Upload Product",
                  bd=2,
                  font=controller.norml_font,
                  padx=15,
                  pady=3,
                  bg=controller.button_color,
                  fg="white",
                  relief=tk.RIDGE, command=self.upload_tool_info).grid(row=7, column=0, columnspan=7, pady=(40, 0))

        tk.Label(self, text="Upload Image:",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=1, column=3, pady=(40, 2), padx=(0, 20), sticky="e")

        ### Here is button to upload image from user
        ### This only will take the path of image and then with the function
        ### we can copy this path to our data base including image
        tk.Button(self, text="Browse Image",
                  bd=2,
                  font=controller.norml_font,
                  padx=0,
                  pady=0,
                  bg=controller.button_color,
                  fg="white",
                  relief=tk.RIDGE, command=self.upload_img).grid(row=1, column=4, pady=(40, 2), sticky="w")

        tk.Label(self, text="Description* :",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=2, column=3, pady=(30, 2), padx=(0, 20), sticky="e")

        self.text_Description = tk.Text(self, height=8, width=25)
        self.text_Description.grid(row=2, rowspan=3, column=4, pady=(30, 2), sticky="w")

        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(23, 0), row=9, column=0, columnspan=7, sticky="nsew")

    def isDetailsValid(self):
        cond1 = len(str(self.Product_Name_entry.get())) > 4
        cond2 = False
        try:
            if self.Delivery_Cost_entry.get() != "":
                float(self.Delivery_Cost_entry.get())
            float(self.Product_Price_entry.get())
            date = self.Available_Date_entry.get()
            date_format = '%Y-%m-%d'
            datetime.datetime.strptime(date, date_format)
            if tool.str_to_date(date) < (datetime.date.today() + datetime.timedelta(6 * 7)) and tool.str_to_date(
                    date) > datetime.date.today():
                cond2 = True
        except ValueError:
            return False
        cond3 = len(str(self.Location_entry.get())) > 4
        return cond1 and cond2 and cond3

    def postupdate(self):
        self.Product_Name_entry.focus()

    def goback_func(self):
        self.Product_Name_entry.delete(0, "end")
        self.Delivery_Cost_entry.delete(0, "end")
        self.Available_Date_entry.delete(0, "end")
        self.Product_Price_entry.delete(0, "end")
        self.Location_entry.delete(0, "end")
        self.text_Description.delete(1.0, "end")
        self.error.config(fg="white")
        self.error.grid(row=0, column=0, columnspan=7)

        self.controller.show_frame("Login_succed_main_page")

    def upload_img(self):
        self.img_filename = tk.filedialog.askopenfilename(initialdir="/", title="Select Image",
                                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        ### Fuction which will take all the variale and then add to the database

    def upload_tool_info(self):
        if self.isDetailsValid():
            n = self.Product_Name_entry.get()
            if self.Delivery_Cost_entry.get() == "":
                dc = None
            else:
                dc = self.Delivery_Cost_entry.get()
            ad = self.Available_Date_entry.get()
            p = self.Product_Price_entry.get()
            l = self.Location_entry.get()
            d = self.text_Description.get(1.0, "end")
            if self.img_filename:
                img = True
            else:
                img = False
            details = tool.create_tool_details(n, p, data.current_user.id, ad, l, dc, d, img)
            tl = tool.tool(details)
            tl.offer_tool()
            data.current_user.offered_tools.append(tl)
            self.goback_func()
        else:
            self.error.config(fg="red")
            self.error.grid(row=0, column=0, columnspan=7)


### Here create class for Edit_profile_win
class Edit_profile_win(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Edit_profile_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)
        self.fill_details()

        ### Code for Edit_profile_win
        menu_bg_colors = tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color,
                                  height="3").grid(row=0, column=0, columnspan=7, sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="Make Changes On Your Profile Setting",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        tk.Label(self, font=controller.heading_font,
                 bg=controller.bar_color,
                 fg="white",
                 height="0",
                 width="30").grid(row=1, columnspan=7, pady=(20, 5))
        ### Variable to show the message to User if some thing is wrong in this page
        self.editProfile_msg = tk.StringVar()
        self.editProfile_msg.set("Please Fill Up The Required Fields")

        self.error = tk.Label(self, textvariable=self.editProfile_msg,
                              font=controller.norml_font,
                              bg=controller.bar_color,
                              fg="white"
                              )
        self.error.grid(row=1, column=0, columnspan=7, pady=(20, 5))
        reg_welcome_head = tk.Label(self,
                                    font=controller.heading_font,
                                    bg="#e6e6e6",
                                    height="5",
                                    width="30").grid(row=2, rowspan=6, columnspan=7)
        tk.Label(self, text="New Full Name* :",
                 font=controller.norml_font, bg="#e6e6e6").grid(row=2, column=0, columnspan=3, sticky="e", pady=(15, 0),
                                                                padx=(0, 20))
        tk.Label(self, text="New Email* :",
                 font=controller.norml_font, bg="#e6e6e6").grid(row=3, column=0, columnspan=3, sticky="e", pady=(15, 0),
                                                                padx=(0, 20))
        tk.Label(self, text="New Password* :",
                 font=controller.norml_font, bg="#e6e6e6").grid(row=4, column=0, columnspan=3, sticky="e", pady=(15, 0),
                                                                padx=(0, 20))
        tk.Label(self, text="New Bill Addr* :",
                 font=controller.norml_font, bg="#e6e6e6").grid(row=5, column=0, columnspan=3, sticky="e", pady=(15, 0),
                                                                padx=(0, 20))
        tk.Button(self, text="Update Profile",
                  bd=2,
                  font=controller.norml_font,
                  padx=15,
                  pady=3,
                  bg=controller.button_color,
                  fg="white",
                  relief=tk.RIDGE, command=self.submit_new_profile).grid(row=7, column=0, columnspan=7, pady=(10, 15))
        tk.Label(self, font=controller.heading_font,
                 bg=controller.bar_color,
                 fg="white",
                 height="0",
                 width="30").grid(row=8, columnspan=7, pady=(5, 0))

        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(13, 0), row=9, column=0, columnspan=7, sticky="nsew")

    def postupdate(self):
        self.new_fulname_entry.focus()
        self.fill_details()

    def goback_func(self):
        self.new_fulname_entry.delete(0, "end")
        self.new_email_entry.delete(0, "end")
        self.new_Password_entry.delete(0, "end")
        self.new_BillAddr_entry.delete(0, "end")
        self.error.config(fg="white")
        self.controller.show_frame("Login_succed_main_page")

    def validate_length(self, detail):
        if (len(detail) >= 4):
            return True
        else:
            return False

    def submit_new_profile(self):
        ### Value Stored in these Variables

        fn = str(self.new_fulname_entry.get())
        em = str(self.new_email_entry.get())
        pw = str(self.new_Password_entry.get())
        ba = str(self.new_BillAddr_entry.get())
        cond1 = self.validate_length(fn)
        cond2 = self.validate_length(ba)
        cond3 = self.validate_length(pw)
        cond4 = self.validate_length(em)
        cond_result = cond1 and cond2 and cond3 and cond4
        if cond_result and data.current_user.isValidEmail(em):
            data.current_user.update_details(pw, em, fn, ba)
            self.controller.show_frame("Login_succed_main_page")
            # TODO validate if not same email
        else:
            self.error.config(fg="red")

    def fill_details(self):
        self.newBAddress = tk.StringVar()
        self.newBAddress.set(str(data.current_user.billing_address))
        self.newPassword = tk.StringVar()
        self.newPassword.set(str(data.current_user.password))
        self.newEmail = tk.StringVar()
        self.newEmail.set(str(data.current_user.email))
        self.newFullName = tk.StringVar()
        self.newFullName.set(str(data.current_user.full_name))
        self.new_BillAddr_entry = tk.Entry(self,
                                           font=self.controller.sml_entry_height, width="28",
                                           textvariable=self.newBAddress)
        self.new_BillAddr_entry.grid(row=5, column=3, columnspan=3, sticky="w", pady=(15, 15))
        self.new_Password_entry = tk.Entry(self,
                                           font=self.controller.sml_entry_height, width="28",
                                           textvariable=self.newPassword)
        self.new_Password_entry.grid(row=4, column=3, columnspan=3, sticky="w", pady=(15, 0))
        self.new_email_entry = tk.Entry(self,
                                        font=self.controller.sml_entry_height, width="28", textvariable=self.newEmail)
        self.new_email_entry.grid(row=3, column=3, columnspan=3, sticky="w", pady=(15, 0))
        self.new_fulname_entry = tk.Entry(self,
                                          font=self.controller.sml_entry_height, width="28",
                                          textvariable=self.newFullName)
        self.new_fulname_entry.grid(row=2, column=3, columnspan=3, sticky="w", pady=(15, 0))


### Here create class for Invoces_window
class Invoces_window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Invoces_window frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)

        self.list_of_invoices = []
        self.contents = dict()
        for x in data.current_user.invoices:
            self.list_of_invoices.append(x.uid)
            self.contents[str(x.uid)] = x.getText()
        self.cnames = tk.StringVar(value=self.list_of_invoices)

        ### Code for Offer_new_tool_win
        tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color, height="3").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(16, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=5,
                                                                                                  sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="All Your Invoives is Listed Here",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        tk.Label(self, text="Select Your Invoice And Press Show To See Your Invoices",
                 font=controller.norml_font, bg=controller.bg_color
                 ).grid(row=2, rowspan=1, column=0, columnspan=7, pady=(20, 0))

        ### Adding ListBox
        ### Here getting list from the folder, that i created for demo check
        ### all the invoices are comming from that folder called demo_Invoices.
        self.List_Box = tk.Listbox(self, width=10, height=17, listvariable=self.cnames)
        self.List_Box.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=(100, 0), pady=(25, 5))
        ### Setting scroll bar
        self.scrlbar = tk.Scrollbar(self, orient="vertical", command=self.List_Box.yview)
        self.List_Box.configure(yscrollcommand=self.scrlbar.set)
        self.scrlbar.grid(column=0, columnspan=2, row=3, sticky="ens", pady=(25, 5))
        ### Adding mesage_box
        self.text = tk.StringVar()
        self.Invoice_mesg_box = tk.Text(self, width=10, height=17)
        self.Invoice_mesg_box.grid(row=3, column=2, columnspan=7, sticky="nsew", padx=100, pady=(25, 5))
        ##        self.Invoice_mesg_box.config(state=tk.DISABLED)

        Cancel_butn = tk.Button(self,
                                text="Cancel",
                                bd=2,
                                font=controller.back_btn_fnt,
                                padx=10,
                                pady=0,
                                bg=controller.button_color,
                                fg="white",
                                relief=tk.RIDGE, command=self.cancel_button)
        Cancel_butn.grid(row=3, column=2, sticky="sw", padx=10, pady=(0, 75))

        show_butn = tk.Button(self,
                              text="Show",
                              bd=2,
                              font=controller.back_btn_fnt,
                              padx=10,
                              pady=0,
                              bg=controller.button_color,
                              fg="white",
                              relief=tk.RIDGE, command=self.open_selected_invoice)
        show_butn.grid(row=3, column=2, sticky="nw", padx=10, pady=(75, 0))
        tk.Label(self, bg=controller.bg_color).grid(row=5, pady=(30, 0))
        ### Footer
        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(10, 0), row=6, column=0, columnspan=7, sticky="nsew")

        ### Folder Path to show the Invoices to the User

    def funt_to_return_selected_invoice_name(self):
        self.file_name = self.List_Box.get(self.List_Box.curselection())
        return self.file_name

    def open_selected_invoice(self):
        try:
            self.cancel_button()
            self.file_name = self.funt_to_return_selected_invoice_name()
            self.Invoice_mesg_box.insert(1.0, self.contents[self.file_name])
        except tk.TclError:
            print("no selection")

    def cancel_button(self):
        self.Invoice_mesg_box.delete(1.0, "end")

    def postupdate(self):
        pass

    def goback_func(self):
        self.Invoice_mesg_box.delete(1.0, "end")
        self.controller.show_frame("Login_succed_main_page")


### Here create class for hired tool windows
class Hired_tool_win(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Hired_tool_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)

        ### Code for Hired_tool_win
        tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color, height="3").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(8, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=5,
                                                                                                  sticky="nsew")
        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="These Tools Are Hired By You",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        ### Bring here User's Tools Data, the given below is just temporary data
        self.tree_col_heading = ("Product Name", "Product Price", "Product Location")
        self.tree_data = dict()
        self.tools_data = []

        ### Setting font size of column heading etc.
        self.tree_style = ttk.Style()
        self.tree_style.configure("Treeview.Heading", font=controller.norml_font)
        self.tree_style.configure("Treeview", font="arial 13", rowheight=30)
        ### Setting column text alignment to the center
        self.generateTree()
        ### This loop is assignig value of heading from the varibale tree_col_heading
        for col in self.tree_col_heading:
            self.tree.heading(col, text=col.title())

        ### This loop is assignig value of column and row from the varibale self.tree_data

        tk.Label(self, text="Select The Given Tool And Press Button To Return The Tools",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=4, column=0, columnspan=7, sticky="w", padx="100", pady=5)

        return_Tool_btn = tk.Button(self, text="Return Tool",
                                    bd=2,
                                    font=controller.norml_font,
                                    padx=15,
                                    pady=3,
                                    bg=controller.button_color,
                                    fg="white",
                                    relief=tk.RIDGE, command=self.YesOrNO)
        return_Tool_btn.grid(pady=5, row=4, column=0, columnspan=7, sticky="e", padx="100")

        view_Tool_btn = tk.Button(self, text="View tool's details",
                                  bd=2,
                                  font=controller.norml_font,
                                  padx=15,
                                  pady=3,
                                  bg=controller.button_color,
                                  fg="white",
                                  relief=tk.RIDGE, command=self.showDetails)
        view_Tool_btn.grid(pady=5, row=5, column=0, columnspan=7, sticky="e", padx="100")

        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(18, 0), row=6, column=0, columnspan=7, sticky="nsew")

    def showDetails(self):
        try:
            selected = self.tree.selection()[0]
            selected_tool = None
            for x in data.current_user.hired_tools:
                if x.details['name'] == self.tree.item(selected)['values'][0]:
                    selected_tool = x
                    break
            all_frames["Specific_tool_detail_win"].set_tool(x, "Hired_tool_win")
            self.controller.show_frame("Specific_tool_detail_win")
        except IndexError:
            print("no selection done")

    def YesOrNO(self):
        try:
            MsgBox = messagebox.askquestion('Return Your Tool ???', 'Are you sure you want to Return your Tool ???')
            if MsgBox == "yes":
                selected = self.tree.selection()[0]
                for x in data.current_user.hired_tools:
                    if x.details['name'] == self.tree.item(selected)['values'][0]:
                        x.request_return()
                        self.generateTree()
                        break
        except IndexError:
            print("no selection done")

    def generateTree(self):
        self.tree = ttk.Treeview(self, columns=self.tree_col_heading, show="headings")
        self.tree.grid(column=0, columnspan=7, row=2, sticky='nsew', pady=(15, 5), padx="100")
        self.tree.column(0, anchor=tk.S)
        self.tree.column(1, anchor=tk.S)
        self.tree.column(2, anchor=tk.S)

        self.scrlbar = tk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrlbar.set)

        self.scrlbar.grid(column=0, columnspan="7", row=2, sticky="ens", pady=(15, 5), padx="100")
        for x in data.current_user.hired_tools:
            if x.details['is_return_accepted'] == True:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('returned'))
            elif x.details['return_date'] != None:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('requested'))
            else:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('hired'))

        self.tree.tag_configure('returned', background='green')
        self.tree.tag_configure('requested', background='orange')
        self.tree.tag_configure('hired', background='red')

    def postupdate(self):
        self.generateTree()
        self.tree.grid(column=0, columnspan=7, row=2, sticky='nsew', pady=(15, 5), padx="100")

    def goback_func(self):
        self.tree.selection_remove(self.tree.focus())
        self.controller.show_frame("Login_succed_main_page")


### Here create class for Available tools  windows
class Available_tool_win(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Available_tool_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)

        ### Code for Available_tool_win
        tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color, height="3").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(8, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=5,
                                                                                                  sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="This Is The List Of All Available Tools",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        ### Bring here User's Tools Data, the given below is just temporary data
        self.update()

        tk.Label(self, text="Select The Given Tool And Press Button To Book Tools",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=4, column=0, columnspan=7, sticky="w", padx="100", pady=5)

        self.return_Tool_btn2 = tk.Button(self, text="Book Tool",
                                          bd=2,
                                          font=controller.norml_font,
                                          padx=15,
                                          pady=3,
                                          bg=controller.button_color,
                                          fg="white",
                                          relief=tk.RIDGE, command=self.YesOrNO2)
        self.return_Tool_btn2.grid(pady=5, row=4, column=0, columnspan=7, sticky="e", padx="100")

        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(18, 0), row=6, column=0, columnspan=7, sticky="nsew")
        ###########################################

        tk.Label(self, text="Hire to Date YYYY-MM-DD:",
                 font=controller.norml_font, bg=controller.bg_color,
                 ).grid(row=5, column=3, pady=(30, 2), padx=(0, 20), sticky="e")

        self.Available_Date_entry = tk.Entry(self,
                                             font=controller.sml_entry_height,
                                             width="25")
        self.Available_Date_entry.grid(row=5, column=4, pady=(30, 2), sticky="w")

        self.half_day = tk.IntVar()
        tk.Checkbutton(
            self, text="Hire for half day?",
            variable=self.half_day).grid(row=5, column=0, pady=(30, 2), sticky="w")

        self.transportTo = tk.IntVar()
        tk.Checkbutton(
            self, text="Delivery To?",
            variable=self.transportTo).grid(row=5, column=1, pady=(30, 2), sticky="w")
        self.tranportFrom = tk.IntVar()
        tk.Checkbutton(
            self, text="Delivery From?",
            variable=self.tranportFrom).grid(row=5, column=2, pady=(30, 2), sticky="w")

    def update(self):
        self.tree_col_heading2 = ("Tool Name", "Price", "Location", "Available Date")
        self.tree_data2 = []
        for x in data.current_user.available_tools:
            self.tree_data2.append([str(x.details['name']), str(x.details['price']), str(x.details['location']),
                                    str(x.details['available_due'])])

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

    def YesOrNO2(self):
        try:
            if self.validateDetails():
                MsgBox = messagebox.askquestion('To Book', 'Plese Click on Ok tO Confirm Booking')
                if MsgBox == "yes":
                    selected = self.tree2.selection()[0]
                    for x in data.current_user.available_tools:
                        if x.details['name'] == self.tree2.item(selected)['values'][0]:
                            date = tool.str_to_date(self.Available_Date_entry.get())
                            x.hire_tool(data.current_user.id, date, self.half_day.get(), self.transportTo.get(),
                                        self.tranportFrom.get())
                            data.current_user.hired_tools.append(x)
                            data.current_user.available_tools.remove(x)
                            self.tree2.delete(selected)
                            self.controller.show_frame("Hired_tool_win")
                            break
            else:
                self.return_Tool_btn2.config(fg="red")
        except IndexError:
            print("no selection done")

    def validateDetails(self):
        cond2 = False
        date = self.Available_Date_entry.get()
        try:
            date_format = '%Y-%m-%d'
            datetime.datetime.strptime(date, date_format)
            cond2 = True
        except ValueError:
            return False
        cond1 = tool.str_to_date(date) > datetime.date.today()
        cond3 = tool.str_to_date(date) < (datetime.date.today() + datetime.timedelta(3))
        print(cond1)
        print(cond2)
        print(cond3)
        if cond2 and cond3 and cond1:
            return True
        else:
            return False

    def get_selected_value_from_treeview2(self):
        select_item2 = self.tree2.focus()
        selected_item2 = self.tree2.item(select_item2)
        print(selected_item2)
        self.tree2.selection_remove(self.tree2.focus())

    def postupdate(self):
        self.return_Tool_btn2.config(fg="white")
        self.update()

    def goback_func(self):
        self.tree2.selection_remove(self.tree2.focus())
        self.return_Tool_btn2.config(fg="white")
        self.controller.show_frame("Login_succed_main_page")


### Here create class for Offered tools
class Offered_tool_win(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.requested = []
        self.editable = []
        ###  Offered_tool_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)

        ### Code for Offered_tool_win
        tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color, height="3").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(16, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=5,
                                                                                                  sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="Thsese Are The Tools Offered By You",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        tk.Label(self, text="In The Given List These Are Your's Offered Tools",
                 font=controller.norml_font, bg=controller.bg_color
                 ).grid(row=2, rowspan=1, column=0, columnspan=7, pady=(20, 0))
        self.tree_col_heading = ("Product Name", "Product Price", "Product Location")

        ### main VARIABLE whre we will get all this list of user's Tools
        '''self.list=tk.StringVar()
        self.list.set("Product1 Product2 Product3 Product4 Product5")
        self.List_Box = tk.Listbox(self,width=10,height=10,listvariable=self.list)
        self.List_Box.grid(row=3,column=0,columnspan=6,sticky="nsew",padx=(100,0),pady=(25,5))
        self.List_Box.config(font="arial 15 bold")
        ### Setting scroll bar
        self.scrlbar = tk.Scrollbar(self,orient="vertical", command=self.List_Box.yview)
        self.List_Box.configure(yscrollcommand=self.scrlbar.set)
        self.scrlbar.grid(column=0,columnspan=6,row=3 ,sticky="ens",pady=(25,5))'''
        self.generateTree()
        for col in self.tree_col_heading:
            self.tree.heading(col, text=col.title())

        Offered_Tools_win = tk.Button(self,
                                      text="View tool's details",
                                      bd=2,
                                      font=controller.norml_font,
                                      padx=15,
                                      pady=3,
                                      bg=controller.button_color,
                                      fg="white",
                                      relief=tk.RIDGE, command=self.showDetails)
        Offered_Tools_win.grid(row=4, column=0, columnspan=7, pady=10, sticky="e", padx=(0, 125))

        return_request_window = tk.Button(self,
                                          text="View Return Request",
                                          bd=2,
                                          font=controller.norml_font,
                                          padx=15,
                                          pady=3,
                                          bg=controller.button_color,
                                          fg="white",
                                          relief=tk.RIDGE, command=self.view_request)
        return_request_window.grid(row=4, column=0, columnspan=7, pady=10, sticky="w", padx=(100, 0))
        ### Footer
        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(27, 0), row=6, column=0, columnspan=7, sticky="nsew")

    def showDetails(self):
        try:
            selected = self.tree.selection()[0]
            selected_tool = None
            for x in data.current_user.offered_tools:
                if x.details['name'] == self.tree.item(selected)['values'][0]:
                    selected_tool = x
                    break
            all_frames["Specific_tool_detail_win"].set_tool(x, "Offered_tool_win")
            self.controller.show_frame("Specific_tool_detail_win")
        except IndexError:
            print("no selection done")

    def view_request(self):
        try:
            selected = self.tree.selection()[0]
            for x in data.current_user.offered_tools:
                if x in self.requested:
                    if x.details['name'] == self.tree.item(selected)['values'][0]:
                        all_frames['Return_requested_window'].set_tool(x)
                        self.controller.show_frame("Return_requested_window")
                        break
        except IndexError:
            print("no selection done")

    def postupdate(self):
        self.generateTree()
        self.tree.grid(column=0, columnspan=7, row=2, sticky='nsew', pady=(15, 5), padx="100")

    def goback_func(self):
        self.controller.show_frame("Login_succed_main_page")

    def generateTree(self):
        self.tree = ttk.Treeview(self, columns=self.tree_col_heading, show="headings")
        self.tree.grid(column=0, columnspan=7, row=2, sticky='nsew', pady=(15, 5), padx="100")
        self.tree.column(0, anchor=tk.S)
        self.tree.column(1, anchor=tk.S)
        self.tree.column(2, anchor=tk.S)

        self.scrlbar = tk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrlbar.set)

        self.scrlbar.grid(column=0, columnspan="7", row=2, sticky="ens", pady=(15, 5), padx="100")
        for x in data.current_user.offered_tools:
            if x.details['return_date'] == None and x.details['is_hired'] == True:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('hired'))
            elif x.details['return_date'] != None and x.details['is_return_accepted'] == None and x.details[
                'is_hired'] == True:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('requested'))
                self.requested.append(x)
            elif x.details['is_return_accepted'] == False:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('damaged'))
            elif x.details['return_date'] != None and x.details['is_return_accepted'] == True:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('returned'))
            else:
                self.tree.insert('', 'end',
                                 values=[str(x.details['name']), str(x.details['price']), str(x.details['location'])],
                                 tags=('available'))
                self.editable.append(x)

        self.tree.tag_configure('returned', background='green')
        self.tree.tag_configure('available', background='pink')
        self.tree.tag_configure('hired', background='yellow')
        self.tree.tag_configure('damaged', background='red')
        self.tree.tag_configure('requested', background='orange')


### Here create class for Specific_tool_detail_win
class Specific_tool_detail_win(tk.Frame):

    def set_tool(self, tool, window):
        self.show_tool = tool
        self.window = window
        self.list_col_2 = []
        self.list_col_2.append(str(self.show_tool.details['name']))
        self.list_col_2.append(str(self.show_tool.details['price']))
        self.list_col_2.append(str(self.show_tool.details['location']))
        self.list_col_2.append(str(self.show_tool.details['hire_from_date']))
        self.list_col_2.append(str(self.show_tool.details['delivery_cost']))
        self.list_col_2.append(str(self.show_tool.details['hired_to_date']))
        self.list_col_2.append(str(self.show_tool.details['description']))
        self.list2 = tk.StringVar()
        self.list2.set(self.list_col_2)
        self.list2 = tk.StringVar()
        self.list2.set(self.list_col_2)
        self.listbox2 = tk.Listbox(self, listvariable=self.list2, bd=1, height=9, font=("arial", 19), width=26,
                                   justify="center")
        self.listbox2.grid(row=3, columnspan=7, pady=(0, 40), sticky="e", padx=108)
        self.listbox2.grid(row=3, columnspan=7, pady=(0, 40), sticky="e", padx=108)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Specific_tool_detail_win frame setting
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)

        ### Code for Specific_tool_detail_win
        tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color, height="3").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(8, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=5,
                                                                                                  sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="This Is The Info Of Your Selected Tool ",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        tk.Label(self, text="Selected Product", font=controller.heading_font,
                 bg=controller.bar_color,
                 fg="white",
                 height="0",
                 width="27").grid(row=1, columnspan=7, pady=(20, 2), sticky="w", padx=100)

        ### Add this list in the Loop so the can Work Correctly temporary i set then like this:
        self.list_col_1 = "Product_Name Product_Price Product_Location Start_Date Product_Delivery_Cost End_Date Product_Description "
        self.list1 = tk.StringVar()
        self.list1.set(self.list_col_1)
        self.listbox1 = tk.Listbox(self, listvariable=self.list1, bd=1, height=9, font=("arial", 19), width=26,
                                   justify="center")
        self.listbox1.grid(row=3, columnspan=7, pady=(0, 40), sticky="w", padx=108)

        tk.Label(self, text="Given Detail By Owner", font=controller.heading_font,
                 bg=controller.bar_color,
                 fg="white",
                 height="0",
                 width="27").grid(row=1, columnspan=7, pady=(20, 2), sticky="e", padx=100)

        ### Add this list in the Loop so the can Work Correctly temporary i set then like this:
        # self.list_col_2 = "Window Is_400€ Luton 12/02/2012 399€ 12/02/2012 Description_Go_Here"

        ### Footer
        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(28, 0), row=6, column=0, columnspan=7, sticky="nsew")

    def postupdate(self):
        pass

    def goback_func(self):
        self.controller.show_frame(self.window)


### Here create class for Return_requested_window
class Return_requested_window(tk.Frame):
    def set_tool(self, tool=None):
        self.show_tool = tool

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###  Return_requested_window frame setting
        self.set_tool()
        self.controller = controller
        controller.grid_columnconfigure(0, weight=1)
        controller.grid_rowconfigure(0, weight=1)
        self.img_filename = None
        ### Code for Return_requested_window
        tk.Label(self, font=controller.menu_buton_font, width="105", bg=controller.bar_color, height="3").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=7,
                                                                                                               sticky="nsew")
        tk.Label(self, font=controller.menu_buton_font, bg=controller.bg_color, height="10").grid(pady=(8, 0), padx=20,
                                                                                                  row=1, column=0,
                                                                                                  columnspan=7,
                                                                                                  rowspan=6,
                                                                                                  sticky="nsew")

        go_back_butn = tk.Button(self,
                                 text="Go Back",
                                 bd=2,
                                 font=controller.back_btn_fnt,
                                 padx=0,
                                 pady=0,
                                 bg=controller.button_color,
                                 fg="white",
                                 relief=tk.RIDGE, command=self.goback_func)
        go_back_butn.grid(row=0, column=0, sticky="w", padx=(20, 0))

        tk.Label(self, text="Here You Can Return Your Tool",
                 font=controller.norml_font,
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=0, column=0, columnspan=7)

        tk.Label(self, text="", font=controller.heading_font,
                 bg=controller.bar_color,
                 height="0",
                 width="30").grid(row=1, columnspan=7, pady=(20, 2), sticky="nsew", padx=100)

        tk.Label(self, text="Below Please Enter Description Of Product",
                 font="Verdana 13 bold",
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=1, column=0, columnspan=7, pady=(20, 2), padx=100, sticky="nsew")

        self.return_text_Description = tk.Text(self, height=8, width=25)
        self.return_text_Description.grid(row=2, column=0, columnspan=7, pady=(10, 2), sticky="nsew", padx=100)

        tk.Label(self, text="",
                 font="Verdana 13 bold",
                 bg=controller.bar_color,
                 fg="white"
                 ).grid(row=4, column=0, columnspan=7, pady=(10, 2), padx=100, sticky="nsew")

        tk.Label(self, text="Important* : Please Choose Image Of The Product From Your Computer",
                 font="Verdana 11 bold",
                 bg=controller.bg_color,
                 ).grid(row=5, column=0, columnspan=7, pady=(10, 2), padx=100, sticky="w")

        select_img = tk.Button(self, text="Upload Image",
                               bd=2,
                               font=controller.norml_font,
                               padx=0,
                               pady=0,
                               bg=controller.button_color,
                               fg="white",
                               relief=tk.RIDGE, command=self.return_upload_img)
        select_img.grid(row=5, column=0, columnspan=7, pady=(10, 2), sticky="e", padx=100)

        accept_btn = tk.Button(self, text="Accept",
                               bd=2,
                               font=controller.norml_font,
                               padx=25,
                               pady=2,
                               bg=controller.button_color,
                               fg="white",
                               relief=tk.RIDGE, command=self.Acept_button)
        accept_btn.grid(row=6, column=0, columnspan=7, pady=(30, 15), sticky="e", padx=100)

        cancel_btn = tk.Button(self, text="Reject",
                               bd=2,
                               font=controller.norml_font,
                               padx=25,
                               pady=2,
                               bg=controller.button_color,
                               fg="white",
                               relief=tk.RIDGE, command=self.Cancel_button)
        cancel_btn.grid(row=6, column=0, columnspan=7, pady=(30, 15), sticky="w", padx=100)

        ### Footer
        menu_bg_color = tk.Label(self, font=controller.menu_buton_font, height="4", bg=controller.bar_color).grid(
            pady=(30, 0), row=8, column=0, columnspan=7, sticky="nsew")

    def return_upload_img(self):
        self.img_filename = tk.filedialog.askopenfilename(initialdir="/", title="Select Image",
                                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    def postupdate(self):
        self.return_text_Description.focus_set()

    def goback_func(self):
        self.controller.show_frame("Offered_tool_win")

    def Acept_button(self):
        self.show_tool.return_tool()
        self.controller.show_frame("Offered_tool_win")

    def Cancel_button(self):
        if self.img_filename:
            a = True
        else:
            a = False
        self.show_tool.damage_tool(str(self.return_text_Description.get(1.0, "end")), a)
        self.controller.show_frame("Offered_tool_win")


### Function to call from the other class
global fun_login_succeed


def fun_login_succeed():
    Registered_User_Windows = Login_Succeed()
    Registered_User_Windows.config(bg="#EAE9E9")
    ##	Registered_User_Windows.resizable(False,False)
    Registered_User_Windows.geometry("960x540")
    Registered_User_Windows.title("Welcome to Shared Power")
    Registered_User_Windows.grid_propagate(1)
    global all_frames
    all_frames = Registered_User_Windows.frames
    Registered_User_Windows.mainloop()


if __name__ == "__main__":
    fun_login_succeed()
