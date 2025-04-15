import tkinter as tk
import customtkinter as ctk
from PIL import Image
import ast
from tkinter import messagebox
from Methods import database as db, text_to_speech as tts, AI_api as ai, passwordCheck as pc, YT_trans as tran, pdf
import threading



ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")

        self.title("")
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.current_user = None

        self.pages = {
            "login": Login(self.container, self),
            "signup": SignUp(self.container, self),
            "password-reset": PasswordReset(self.container, self),
            "homepage": HomePage(self.container, self)
        }

        self.display_page("login")

    def display_page(self, page_name):
        for page in self.container.winfo_children():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)

        if page_name == "homepage" and self.current_user:
            self.pages["homepage"].update_user_data(self.current_user)

class Login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.fg_color = "#030f0f"
        self.accent_color = "#03624c"
        self.font_large = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")
        self.font_medium = ctk.CTkFont(family="Segoe UI", size=16)
        self.font_small = ctk.CTkFont(family="Segoe UI", size=12)

        self.create_page()

    def create_page(self):

        self.controller.title("Login")
        self.container = ctk.CTkFrame(self, width=410, height=475, corner_radius=18, fg_color=self.fg_color,
                                 bg_color="transparent", border_width=1, border_color="grey23")
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        p1 = ctk.CTkLabel(self.container, text="Login", font=self.font_large, anchor=tk.CENTER)
        p1.place(x=125, y=28)

        p2 = ctk.CTkLabel(self.container, text="Username", font=self.font_small)
        p2.place(x=55, y=140)
        self.username_input = ctk.CTkEntry(self.container, placeholder_text="username", width=300, height=50)
        self.username_input.place(x=55, y=166)

        p3 = ctk.CTkLabel(self.container, text="Password", font=self.font_small)
        p3.place(x=55, y=230)
        self.password_input = ctk.CTkEntry(self.container, placeholder_text="password", width=300, height=50, show="*")
        self.password_input.place(x=55, y=256)

        forgot = ctk.CTkLabel(self.container, text="Forgot password?", cursor="hand2", font=self.font_small, text_color='blue')
        forgot.place(x=258, y=306)
        forgot.bind("<Button-1>", lambda event: self.controller.display_page("password-reset"))


        login_button = ctk.CTkButton(self.container, text="Login", width=300, height=40, corner_radius=50,
                                     fg_color=self.accent_color, hover_color="#8A9A5B" ,command=self.login)
        login_button.place(x=55, y=360)


        p4 = ctk.CTkLabel(self.container, text="Don't have an account?", font=self.font_small)
        p4.place(x=181, y=400)

        create_account = ctk.CTkLabel(self.container, text="Register", cursor="hand2", font=self.font_small, text_color="blue")
        create_account.place(x=306, y=400)
        create_account.bind("<Button-1>", lambda event: self.controller.display_page("signup"))

    def login(self):
        username = self.username_input.get().strip()
        password = self.password_input.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in the full form" )
            self.highlight_field(username, password)
        else:
            if not db.login_check(username, password):
                messagebox.showwarning("Incorrect Information", "Wrong user or password.\nPlease create an account!")
            else:
                self.controller.current_user = {'username': username, 'id': db.get_user_id(username, password)}
                self.controller.display_page("homepage")

        if username and not db.user_check(username):
            messagebox.showerror("Error", "This user doesn't exit in the data base")

    def highlight_field(self, username, password):
        if not username:
            self.username_input.configure(border_width=2, border_color="red")
        else:
            self.username_input.configure(border_width=0, border_color="")

        if not password:
            self.password_input.configure(border_width=2, border_color="red")
        else:
            self.password_input.configure(border_width=0, border_color="")

class SignUp(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        self.fg_color = "#030f0f"
        self.accent_color = "#03624c"
        self.font_large = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")
        self.font_medium = ctk.CTkFont(family="Segoe UI", size=16)
        self.font_small = ctk.CTkFont(family="Segoe UI", size=12)


        self.create_page()

    def create_page(self):
        self.controller.title("Signup")

        self.container = ctk.CTkFrame(self, width=410, height=590, corner_radius=18, fg_color=self.fg_color,
                                 bg_color="transparent")
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        p1 = ctk.CTkLabel(self.container, text="Sign Up", font=self.font_large, anchor=tk.CENTER)
        p1.place(x=95, y=28)


        self.login_input = ctk.CTkEntry(self.container, placeholder_text="Enter Your Username", width=300, height=45)
        self.login_input.place(x=55, y=140)


        self.password_input = ctk.CTkEntry(self.container, placeholder_text="Enter Your Password", width=300, height=45, show="*")
        self.password_input.place(x=55, y=200)


        self.password_confirm_input = ctk.CTkEntry(self.container, placeholder_text="Confirm Your Password", width=300, height=45, show="*")
        self.password_confirm_input.place(x=55, y=260)


        self.secret_question = ctk.CTkOptionMenu(self.container, values=[
            "What’s your favorite artist?",
            "What is your favorite sport?",
            "What is your mother’s phone number?",
            "What's your favorite color?",
            "How many pets did you have at 10 years old?"
        ], width=300, height=45, fg_color="grey22", button_color="grey22")
        self.secret_question.place(x=55, y=320)


        self.question_answer = ctk.CTkEntry(self.container, placeholder_text="Write Your Answer Here", width=300, height=45)
        self.question_answer.place(x=55, y=380)


        signup_button = ctk.CTkButton(self.container, text="Sign up", width=300, height=40, corner_radius=50,
                                      fg_color=self.accent_color, command=self.add_user)
        signup_button.place(x=55, y=465)


        p4 = ctk.CTkLabel(self.container, text="Already have an account?", font=self.font_small)
        p4.place(x=183, y=505)

        create_account = ctk.CTkLabel(self.container, text="Login", cursor="hand2", font=self.font_small, text_color="blue")
        create_account.place(x=322, y=505)
        create_account.bind("<Button-1>", lambda event: self.controller.display_page("login"))

    def add_user(self):
        username = self.login_input.get().strip()
        password = self.password_input.get().strip()
        password_confirm=self.password_confirm_input.get().strip()
        question = self.secret_question.get().strip()
        answer = self.question_answer.get().strip()

        self.reset_fields()

        if not username or not password or not answer or not password_confirm:
            messagebox.showerror("Error", "Please fill in the full form")
            self.highlight_field(username, password, password_confirm, answer)
            return

        if username and db.user_check(username):
            messagebox.showwarning("Warning", "User already exists")
            self.login_input.configure(border_width=2, border_color="red")
            return


        if password != password_confirm:
            messagebox.showerror("Error", "Password doesn't match")
            self.password_input.configure(border_width=2, border_color="red")
            self.password_confirm_input.configure(border_width=2, border_color="red")
            return

        if pc.check(password):
            messagebox.showwarning("Warning", pc.check(password))
            self.password_input.configure(border_width=2, border_color="red")
            self.password_confirm_input.configure(border_width=2, border_color="red")
            return

        try:
            if db.insert_info(username, password, question, answer):
                messagebox.showinfo("Success", "User has been added successfully")
                self.controller.display_page("login")
            else:
                messagebox.showinfo("Error", "Something went wrong while creating the account")

        except:
            messagebox.showerror("Error", "")

    def highlight_field(self, username, password, password_confirm, answer):
        if not username:
            self.login_input.configure(border_width=2, border_color="red")
        else:
            self.login_input.configure(border_width=0, border_color="")

        if not password:
            self.password_input.configure(border_width=2, border_color="red")
        else:
            self.password_input.configure(border_width=0, border_color="")

        if not password_confirm:
            self.password_confirm_input.configure(border_width=2, border_color="red")
        else:
            self.password_confirm_input.configure(border_width=0, border_color="")

        if not answer:
            self.question_answer.configure(border_width=2, border_color="red")
        else:
            self.question_answer.configure(border_width=0, border_color="")

    def reset_fields(self):
            self.login_input.configure(border_width=0, border_color="")
            self.password_input.configure(border_width=0, border_color="")
            self.password_confirm_input.configure(border_width=0, border_color="")
            self.question_answer.configure(border_width=0, border_color="")

class PasswordReset(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.fg_color = "#030f0f"
        self.accent_color = "#03624c"
        self.font_large = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")
        self.font_medium = ctk.CTkFont(family="Segoe UI", size=45, weight="bold")
        self.font_small = ctk.CTkFont(family="Segoe UI", size=12)

        self.create_page()


    def create_page(self):
        self.controller.title("Password Reset")

        self.container = ctk.CTkFrame(self, width=410, height=590, corner_radius=18, fg_color=self.fg_color,
                                 bg_color="transparent")
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER, )

        p1 = ctk.CTkLabel(self.container, text="Reset Password", font=self.font_medium, anchor=tk.CENTER)
        p1.place(x=44, y=36)

        self.user_input = ctk.CTkEntry(self.container, placeholder_text="Enter Your Username", width=300, height=45)
        self.user_input.place(x=55, y=140)


        self.secret_question = ctk.CTkOptionMenu(self.container, values=["What’s your favorite artist?",
                                                               "What is your favorite sport?",
                                                               "What is your mother’s phone number?",
                                                               "What's your favorite color?",
                                                               "How many pets did you have at 10 years old?"]
                                            , width=300, height=45, fg_color="grey22", button_color="grey22")
        self.secret_question.place(x=55, y=195)

        self.question_answer = ctk.CTkEntry(self.container, placeholder_text="Write Your Answer Here", width=300, height=50)
        self.question_answer.place(x=55, y=250)

        self.password_input = ctk.CTkEntry(self.container, placeholder_text="New Password", width=300, height=50)
        self.password_input.place(x=55, y=310)

        self.password_confirm_input = ctk.CTkEntry(self.container, placeholder_text="Confirm New Password", width=300, height=50)
        self.password_confirm_input.place(x=55, y=370)

        button = ctk.CTkButton(self.container, text="Reset", width=300, height=40, corner_radius=50, command=self.reset,
                                     fg_color=self.accent_color)
        button.place(x=55, y=470)

        p4 = ctk.CTkLabel(self.container, text="Don't have an account?", font=self.font_small)
        p4.place(x=181, y=510)

        create_account = ctk.CTkLabel(self.container, text="Register", cursor="hand2", font=self.font_small, text_color="blue")
        create_account.bind("<Button-1>", lambda event: self.controller.display_page("login"))
        create_account.place(x=306, y=510)


    def reset(self):
        user = self.user_input.get().strip()
        password = self.password_input.get().strip()
        password_confirm = self.password_confirm_input.get().strip()
        question = self.secret_question.get().strip()
        answer = self.question_answer.get().strip()

        self.reset_fields()

        if not user or not password or not password_confirm or not answer:
            messagebox.showerror("Error", "Please fill in the all the full form" )
            self.highlight_field(user, password, password_confirm, answer)
            if user and not db.user_check(user):
                messagebox.showerror("Error", "This user doesn't exit in the data base")
                return

        elif not db.user_check(user):
            messagebox.showerror("Error", "This user doesn't exit in the data base")

        elif db.user_check(user) and answer and question and not db.check_answer(user, question, answer):
            messagebox.showerror("Error", "Question or answer do not match with this username")
            return

        elif not db.user_check(user) and user:
            messagebox.showerror("Error", "This user doesn't exit in the data base")
            return

        elif password != password_confirm :
            messagebox.showerror("Error", "Password doesn't match")
            self.password_input.configure(border_width=2, border_color="red")
            self.password_confirm_input.configure(border_width=2, border_color="red")
            return

        elif password and password_confirm and pc.check(password):
            messagebox.showerror("warning", pc.check(password))
            return

        elif password and user and question and answer and db.user_check(user) and db.check_answer(user, question, answer):
                db.reset_password(user, password)
                messagebox.showinfo("Information", "Password had been reset successfully")
                self.controller.display_page("login")



    def highlight_field(self, user, password, password_confirm, answer):
            if not user:
                self.user_input.configure(border_width=2, border_color="red")
            else:
                self.user_input.configure(border_width=0, border_color="")

            if not password:
                self.password_input.configure(border_width=2, border_color="red")
            else:
                self.password_input.configure(border_width=0, border_color="")

            if not password_confirm:
                self.password_confirm_input.configure(border_width=2, border_color="red")
            else:
                self.password_confirm_input.configure(border_width=0, border_color="")

            if not answer:
                self.question_answer.configure(border_width=2, border_color="red")
            else:
                self.question_answer.configure(border_width=0, border_color="")

    def reset_fields(self):
            self.user_input.configure(border_width=0, border_color="")
            self.password_input.configure(border_width=0, border_color="")
            self.password_confirm_input.configure(border_width=0, border_color="")
            self.question_answer.configure(border_width=0, border_color="")

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller

        self.user_data = None
        self.chat_id = None

        self.fg_color = "#030f0f"
        self.accent_color = "#03624c"
        self.font_title = ctk.CTkFont(family="Segoe UI", size=40, weight="bold")
        self.font_large = ctk.CTkFont(family="Segoe UI", size=18, weight="bold")
        self.font_medium = ctk.CTkFont(family="Segoe UI", size=17)
        self.font_small = ctk.CTkFont(family="Segoe UI", size=15, weight="bold")

        self.create_page()

    def create_page(self):
        self.controller.title("Home Page")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.rowconfigure(0, weight=1)

        side_menu = ctk.CTkFrame(self, fg_color="grey10")
        side_menu.grid(row=0, column=0, sticky='nsew')

        self.conversation_container = ctk.CTkScrollableFrame(side_menu, height=650, fg_color="grey10", scrollbar_button_color="grey14"
                                               , scrollbar_button_hover_color="grey20")
        self.conversation_container.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.9)

        self.pack_chat()


        def logout():
            self.controller.display_page("login")
            return
        logout_button = ctk.CTkButton(side_menu, text="Logout", font=self.font_large,fg_color='#D22B2B', hover_color="#D2042D", command=logout
                               , width=200, height=45, border_width=0)
        logout_button.pack(side="bottom", pady=15,padx=15, fill="x")

        title = ctk.CTkLabel(side_menu, text="ChatBOT", font=self.font_title)
        title.place(relx=0.5, rely=0.05, anchor="center")

        main_body = ctk.CTkFrame(self, fg_color="grey13")
        main_body.grid(row=0, column=1, sticky='nsew')



        self.chat_body = ctk.CTkScrollableFrame(main_body, fg_color="grey13")
        self.chat_body.pack(fill="both", expand=True)

        input_body = ctk.CTkFrame(main_body, fg_color="grey13", height=200)
        input_body.pack(fill="both")


        def on_focus_in(event):
            if input.get("1.0", "end-1c") == default_text:
                input.delete("1.0", "end")
        def on_focus_out(event):
            if input.get("1.0", "end-1c").strip() == "":
                input.insert("1.0", default_text)

        default_text = "Type your message here..."

        input = ctk.CTkTextbox(input_body, height=120, width=750, corner_radius=20,
                               border_color="grey22", fg_color="grey22", font=self.font_medium)
        input.pack(side="bottom", pady=20)

        input.insert("1.0", default_text)

        input.bind("<FocusIn>", on_focus_in)
        input.bind("<FocusOut>", on_focus_out)

        def print_message(input_text):

            box = ctk.CTkFrame(self.chat_body, fg_color="grey20", corner_radius=15)
            box.pack(side="bottom", anchor="se", pady=20, padx=245)

            message = ctk.CTkLabel(box, text=input_text, wraplength=500, anchor="e", justify="left", font=self.font_medium)
            message.pack(padx=10, pady=5, fill="both")

            input.delete("1.0", "end-1c")

            return input_text

        def reciece_message(text):

            temp = ai.send(text, [])


            if temp.startswith("```python"):
                temp = temp.replace("```python", "").replace("```", "").strip()
            if temp.startswith("```json"):
                temp = temp.replace("```json", "").replace("```", "").strip()

            temp_dict = ast.literal_eval(temp)
            if 1 in temp_dict.keys():
                response = temp_dict.get(1)
                db.insert_message(self.chat_id, 'ai', response)
                box1 = ctk.CTkFrame(self.chat_body, fg_color="grey16")
                box1.pack(side="bottom", anchor="sw", pady=20, padx=245)

                message1 = ctk.CTkLabel(box1, text=response, wraplength=500, anchor="e", justify="left",
                                        font=self.font_medium)
                message1.pack(padx=10, pady=5, fill="both")

            if 2 in temp_dict.keys():

                video_transcribtion = tran.get_transcription(text)
                temp = ai.send("summarize the concept mentioned in this video"  + video_transcribtion, [])

                if temp.startswith("```python"):
                    temp = temp.replace("```python", "").replace("```", "").strip()
                if temp.startswith("```json"):
                    temp = temp.replace("```json", "").replace("```", "").strip()

                temp_dict = ast.literal_eval(temp)

                response = temp_dict.get("1")
                db.insert_message(self.chat_id, 'ai', response)


                box1 = ctk.CTkFrame(self.chat_body, fg_color="grey16")
                box1.pack(side="bottom", anchor="sw", pady=20, padx=245)

                message1 = ctk.CTkLabel(box1, text=response, wraplength=500, anchor="e", justify="left",
                                            font=self.font_medium)
                message1.pack(padx=10, pady=5, fill="both")

        def send():
            input_text = input.get("1.0", "end-1c")
            if input_text == "":
                return

            print_message(input_text)
            db.insert_message(self.chat_id, 'user', input_text)
            threading.Thread(target=reciece_message, args=(input_text,), daemon=True).start()

        def transcribing():
            transcribed_text = tts.listen()
            print_message(transcribed_text)

            threading.Thread(target=reciece_message, args=(transcribed_text,), daemon=True).start()

        icon1 = Image.open("Assets/send.png")
        icon1 = icon1.resize((220, 220), Image.Resampling.LANCZOS)
        arrow_icon = ctk.CTkImage(light_image=icon1,  dark_image=icon1)
        send_button = ctk.CTkButton(input, image=arrow_icon, text="", command=send, height=20,
                                    fg_color="transparent", width=20)
        send_button.place(x=700, y=85)


        icon2 = Image.open("Assets/mic.png")
        icon2 = icon2.resize((220, 220), Image.Resampling.LANCZOS)
        mic_icon = ctk.CTkImage(light_image=icon2, dark_image=icon2)
        mic_button = ctk.CTkButton(input, image=mic_icon, text="", fg_color="transparent"
                                   , command=transcribing, width=10, height=10)
        mic_button.place(x=670, y=85)


        icon3 = Image.open("Assets/delete.png")
        icon3 = icon3.resize((220, 220), Image.Resampling.LANCZOS)
        delete_icon = ctk.CTkImage(light_image=icon3, dark_image=icon3)
        delete_button = ctk.CTkButton(main_body, image=delete_icon, text="Delete", fg_color="grey12"
                                   ,hover_color="#f33939", width=10, height=40, command=lambda: self.delete_chat(self.chat_id))
        delete_button.place(relx=0.95, rely=0.035, anchor='center')





        icon4 = Image.open("Assets/export.png")
        icon4 = icon4.resize((220, 220), Image.Resampling.LANCZOS)
        export_icon = ctk.CTkImage(light_image=icon4, dark_image=icon4)
        export_button = ctk.CTkButton(main_body, image=export_icon, text="Export PDF", fg_color="grey12"
                                    ,hover_color="#8A9A5B", width=10, height=40, command=lambda: self.export_pdf(db.load_messages(self.chat_id)) )
        export_button.place(relx=0.87, rely=0.035, anchor='center')


        icon5 = Image.open("Assets/plus.png")
        icon5 = icon5.resize((220, 220), Image.Resampling.LANCZOS)
        plus_icon = ctk.CTkImage(light_image=icon5, dark_image=icon5)
        plus_button = ctk.CTkButton(side_menu, image=plus_icon, text="New Chat", fg_color="#8A9A5B", text_color='white',
                                      font=self.font_small, hover_color="#8A926B", width=10, height=40, corner_radius=30,
                                    command=self.add_new_convo)
        plus_button.pack(pady=90,padx=20,  side="top", anchor="w")


    def update_user_data(self, user_data):
        self.user_data = user_data
        self.pack_chat()

    def update_chat_id(self, chat_data):
        self.chat_id = chat_data

    def add_new_convo(self):
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("New Chat")
        self.popup.geometry("500x175")
        main_x = self.winfo_x()
        main_y = self.winfo_y()
        x = main_x + (main_x - main_y) // 2
        y = main_y + (main_x - main_y) // 2
        self.popup.geometry(f"+{x}+{y}")


        label = ctk.CTkLabel(self.popup, text="What would you like to name your new chat?", font=self.font_large)
        label.pack(pady=10)

        self.chat_name_input= ctk.CTkEntry(self.popup, width=360, height=40, placeholder_text="Type here")
        self.chat_name_input.pack(pady=8)

        confirm = ctk.CTkButton(self.popup, text="Create", fg_color="#8A9A5B", text_color='white',
                                font=self.font_small, hover_color="#8A926B", width=360, height=40, corner_radius=30,
                                command=self.create_chat)
        confirm.pack(pady=8)

    def create_chat(self):
        name = self.chat_name_input.get().strip()
        if name:
            db.create_new_convo(self.user_data['id'] , name)
            self.popup.destroy()
        self.pack_chat()

    def pack_chat(self):
        if not self.user_data:

            return

        try:
            titles = db.get_all_chat(self.user_data['id'])
            for widget in self.conversation_container.winfo_children():
                widget.destroy()

            for title in titles:
                btn = ctk.CTkButton(self.conversation_container, text=title['title'], font= self.font_medium,
                                     fg_color="grey20", height=50, hover_color="grey28"
                                    ,command=lambda chat_id=title['id']: self.change_chat(chat_id))
                btn.pack(pady=5, fill='x')
        except Exception as e:
            messagebox.showerror("Error", f"Could not load conversations: {e}")

    def change_chat(self, chat_id):
        self.chat_id = chat_id
        self.pack_messages(chat_id)
        return chat_id

    def delete_chat(self, chat_id):
        db.delete_chat(chat_id)
        self.pack_chat()
        return

    def pack_messages(self, chat_id):
        if not db.load_messages(chat_id):
            for widget in self.chat_body.winfo_children():
                widget.destroy()
            return

        messages = db.load_messages(chat_id)
        for page in self.chat_body.winfo_children():
            page.pack_forget()


        for message in messages:
            if message['sender']=='user':
                content = message['content']
                box = ctk.CTkFrame(self.chat_body, fg_color="grey20", corner_radius=15)
                box.pack(side="bottom", anchor="se", pady=20, padx=245)

                message = ctk.CTkLabel(box, text=content, wraplength=500, anchor="e", justify="left",
                                       font=self.font_medium)
                message.pack(padx=10, pady=5, fill="both")

            else:
                content = message['content']
                box1 = ctk.CTkFrame(self.chat_body, fg_color="grey16")
                box1.pack(side="bottom", anchor="sw", pady=20, padx=245)

                message1 = ctk.CTkLabel(box1, text=content, wraplength=500, anchor="e", justify="left",
                                        font=self.font_medium)
                message1.pack(padx=10, pady=5, fill="both")

    def export_pdf(self, chat_id):
        pdf.create_pdf(chat_id)
        return



if __name__ == "__main__":
    app = App()
    app.mainloop()
