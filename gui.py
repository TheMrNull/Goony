import customtkinter as ctk
import random
window = ctk.CTk()
window.geometry("600x800")
window.title("Goony")

ctk.set_appearance_mode("system")

def quit():
    window.destroy()


def button_start():
    button1.configure(text="QUIT", fg_color="green", hover_color="red", command=quit)
    answer = ctk.CTkLabel(window, text="Hi, I'm Goony, and you are...", 
                          bg_color="transparent", font=("Helvetica", 20))
    answer.place(anchor="center", relx=0.5, rely=0.2)
    user_input = ctk.CTkEntry(window, placeholder_text="Type in your name", font=("",12),
                              width=200,
                              height=50,
                          fg_color="yellow", 
                          text_color="black")
    user_input.place(anchor="center", relx=0.5,rely=0.88)
   
    def send_message():
        name = user_input.get()
        res1 = f"Oh {name}... that's such a gooner name, just like mine!"
        res2 = f"Hi {name}, wanna goon together? I'M KIDDING,PULL YOUR PANTS BACK UP !"
        res3 = f"Oh hello {name}, so what's your goon streak? *cough* *cough* ehm I mean, how are you?"
        res = [res1, res2, res3]
        goony_response = random.choice(res)
    send_btn = ctk.CTkButton(window, text="Send", command=send_message, font=("Helvetica", 16))
    send_btn.place(anchor="center", relx=0.8, rely=0.88)
    def settings():
        settings_window = ctk.CTk()
        settings_window.geometry("400x400")
        settings_window.title("Settings")
        def quit_setts():
            settings_window.destroy()
        quit_setts_btn = ctk.CTkButton(settings_window, text="QUIT", command=quit_setts, fg_color="green", hover_color="red")
        quit_setts_btn.place(anchor="center", relx=0.5, rely=0.88)
    settings_btn = ctk.CTkButton(window, text="Settings", font=("Helvetica", 20), command=settings)
    settings_btn.place(anchor="w", relx=0.1, rely=0.88)
button1 = ctk.CTkButton(window, fg_color="red", text="Start chatting", 
                        command=button_start, corner_radius=20, border_width=2, 
                        hover_color="green", border_color="black", width=200, 
                        height=50, font=("Helvetica", 20))
button1.place(anchor="center", relx=0.5, rely=0.95 )







#get away from here
window.mainloop()
###
