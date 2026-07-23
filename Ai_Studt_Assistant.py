import tkinter as tk
from tkinter import messagebox
import os
from groq import Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")

)
messages=[]
CHAT_FILE="chat.txt"
def save_chat():
    chat = response_box.get("1.0",tk.END)
    with open(CHAT_FILE,"w") as file:
        file.write(chat)
    messagebox.showinfo(
        "Success",
        "Chat saved successfully!"
    )
def load_chat():
    try:
        with open(CHAT_FILE,"r")as file:
            data=file.read()
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, data)
        messagebox.showinfo(
        "Success",
        "Chat loaded successfully!"
    )
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved chat found.")
def ask_ai():
    question = question_entry.get("1.0", tk.END).strip()

    if question == "":
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, "Please enter a question.")
        return
    
  
    window.update()
    messages.append(
                {
                    "role": "user",
                    "content": question
                }
    )
    

    try:
        response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
)
        answer = response.choices[0].message.content
        
        
        messages.append(
    {
        "role": "assistant",
        "content": answer
    }
)
        
        response_box.insert(tk.END, "\n")
        response_box.insert(tk.END, "You: " + question + "\n\n")
        response_box.insert(tk.END, "AI: " + answer)
        response_box.insert(tk.END, "\n")
        response_box.insert(tk.END, "-" * 60)
        response_box.insert(tk.END, "\n\n")
        question_entry.delete("1.0", tk.END)

    except Exception as e:
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, f"Error:\n\n{e}")


window = tk.Tk()
window.title("🤖 AI Study Assistant")
window.geometry("700x600")
window.config(bg="#EAF4FF")

dark_mode =False
title = tk.Label(
    window,
    text="🤖 AI Study Assistant",
    font=("Arial", 18, "bold"),
    bg="#EAF4FF"
)
title.pack(pady=10)

question_label = tk.Label(
    window,
    text="Ask your question",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
)

question_label.pack()

question_entry = tk.Text(
    window,
    width=60,
    height=6,
    font=("Arial", 11)
)
question_entry.pack(pady=10)
def clear():
    response_box.delete("1.0", tk.END)


def exit_app():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        window.destroy()

def toggle_theme():
    global dark_mode

    if dark_mode == False:
        dark_mode = True

        window.config(bg="#2C2C2C")
        title.config(bg="#2C2C2C", fg="white")
        theme_button.config(text="☀ Light Mode")

    else:
        dark_mode = False

        window.config(bg="#EAF4FF")
        title.config(bg="#EAF4FF", fg="black")
        theme_button.config(text="🌙 Dark Mode")
ask_button = tk.Button(
    window,
    text="Ask AI",
    command=ask_ai,
    bg="#2196F3",
    fg="white",
    width=20,
    font=("Arial", 11, "bold")
)
ask_button.pack(pady=10)
clear_button = tk.Button(
    window,
    text="Clear Chat",
    command=clear,
    bg="#F44336",
    fg="white",
    width=20,
    font=("Arial", 11, "bold")
)

clear_button.pack(pady=5)
save_button = tk.Button(
    window,
    text="Save Chat",
    command=save_chat,
    bg="#4CAF50",
    fg="white",
    width=20,
    font=("Arial", 11, "bold")
)

save_button.pack(pady=5)
load_button = tk.Button(
    window,
    text="Load Chat",
    command=load_chat,
    bg="#FFC107",
    fg="black",
    width=20,
    font=("Arial", 11, "bold")
)
load_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=exit_app, 
                            bg="red", fg="white", font=("Arial", 12, "bold"))
exit_button.pack(pady=50)

tk.Label(
    window,
    text="AI Response",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
).pack()
theme_button = tk.Button(
    window,
    text="🌙 Dark Mode",
    command=toggle_theme,
    bg="#555555",
    fg="white",
    width=15
)

theme_button.pack(pady=5)

response_box = tk.Text(
    window,
    width=70,
    height=15,
    font=("Arial", 11),
    wrap="word"
)
response_box.pack(pady=10)

load_chat()

window.mainloop()
