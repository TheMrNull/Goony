import tkinter as tk


window = tk.Tk()
window.geometry("600x600")
window.title("Goony")
window.configure(background="black")
window.resizable(False,False)


def first():
    text  = "Hello world"
    text_output = tk.Label(window, text=text, fg='red', font=('Helvetica', 16))
    text_output.grid(row = 0, column=1)

def second_function():
    text = "Nuovo Messaggio! Nuova Funzione!"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, padx=50)

first_button = tk.Button(text="chiedi", command=first)
first_button.grid(row=0, column=0)

second_button = tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20)



#get away from here
if __name__ == "__main__":
    window.mainloop()
###