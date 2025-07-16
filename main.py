#Basic logic of Goony
import random
import tkinter as tk
#REBUILD WITH CTKINTER + ADD A TOGGLE SWITH FOR FREAK MODE 😜 + import ollama
#Window
window = tk.Tk()
window.geometry("800x800")
window.title("Goony")
window.configure(background="black")
window.resizable(False,False)




def quit():
    window.destroy()

def start():
    text = "Hello, I'm Goony, your name is..."
    output = tk.Label(window, text=text, fg='green', font=('Helvetica', 16))
    output.pack(side="top", anchor="center", pady=20)
    start.config(text="QUIT", fg="red", command=quit)

    input_box = tk.Entry(window)
    input_box.pack(side="bottom", anchor="center", pady=30)

    def send_message():
        user_input = input_box.get()
        res1 = f"Oh {user_input}... that's such a gooner name, just like mine!"
        res2 = f"Hi {user_input}, wanna goon together? I'M KIDDING,PULL YOUR PANTS BACK UP !"
        res3 = f"Oh hello {user_input}, so what's your goon streak? *cough* *cough* ehm I mean, how are you?"
        res = [res1, res2, res3]
        goony_response = random.choice(res)
        output.config(text=goony_response)

    send_btn = tk.Button(window, text="Send", command=send_message, font=("Helvetica", 16))
    send_btn.pack(side="bottom", anchor="center", pady=10)
start = tk.Button(text="Start chatting with Goony", command=start, font=("Helvetica", 16))
start.pack(side="bottom", anchor="center", pady=30)




#Stay away from here :), for now

window.mainloop()