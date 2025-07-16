import customtkinter as ctk
import random
import pyfiglet
window = ctk.CTk()
window.geometry("600x800")
window.title("Goony")
art = pyfiglet.figlet_format("Goony")

ctk.set_appearance_mode("system")

def quit():
    window.destroy()

art_display = ctk.CTkLabel(window, text=art, font=("", 30))
art_display.place(anchor="center", relx=0.5,rely=0.5)
def button_start():
    art_display.place_forget()
    button1.configure(text="QUIT", fg_color="green", hover_color="red", command=quit)
    answer = ctk.CTkLabel(window, text="Hi, I'm Goony, and you are...", 
                          bg_color="transparent", font=("Helvetica", 20))
    answer.place(anchor="center", relx=0.5, rely=0.2)
    user_input = ctk.CTkEntry(window, placeholder_text="Type in your name", font=("",18),
                              width=200,
                              height=50,
                          fg_color="yellow", 
                          text_color="black",
                              border_color="black",
                              border_width=3,
                              corner_radius=20)
    user_input.place(anchor="center", relx=0.5,rely=0.85)
   
    def send_message():
        name = user_input.get()
        res1 = f"Oh {name}... that's such a gooner name, just like mine!"
        res2 = f"Hi {name}, wanna goon together? I'M KIDDING,PULL YOUR PANTS BACK UP !"
        res3 = f"Oh hello {name}, so what's your goon streak? *cough* *cough* ehm I mean, how are you?"
        res = [res1, res2, res3]
        goony_response = random.choice(res)
        answer.place_forget()
        msg = ctk.CTkLabel(window, text= goony_response, justify="center", 
                           font=("Helvetica",22),
                           wraplength=200)
        msg.place(anchor="center", relx=0.5, rely=0.5)
        send_btn.configure(state="disabled")
    send_btn = ctk.CTkButton(window, text="Send", command=send_message, font=("Helvetica", 18), 
                             border_color="black", corner_radius=20, border_width=3)
    send_btn.place(anchor="center", relx=0.8, rely=0.85)
    def settings():
        settings_window = ctk.CTk()
        settings_window.geometry("400x400")
        settings_window.title("Settings")
        def quit_setts():
            settings_window.destroy()
        quit_setts_btn = ctk.CTkButton(settings_window, text="QUIT", command=quit_setts, fg_color="green", 
                                       hover_color="red",
                                       border_width=3,
                                       border_color="black",
                                       corner_radius=20)
        quit_setts_btn.place(anchor="center", relx=0.5, rely=0.88)
    settings_btn = ctk.CTkButton(window, text="Settings", font=("Helvetica", 18), command=settings,
                                 border_width=3,
                                 corner_radius=20,
                                 border_color="black")
    settings_btn.place(anchor="w", relx=0.1, rely=0.85)

button1 = ctk.CTkButton(window, fg_color="red", text="Start chatting", 
                        command=button_start, corner_radius=20, border_width=3, 
                        hover_color="green", border_color="black", width=200, 
                        height=50, font=("Helvetica", 20))
button1.place(anchor="center", relx=0.5, rely=0.95 )







#get away from here
window.mainloop()
###
