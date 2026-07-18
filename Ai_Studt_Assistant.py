import tkinter as tk
from tkinter import messagebox
import os
from groq import Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")

)

CHAT_FILE="chat.txt"
def save_chat():
    chat = response_box.get("1.0",tk.END)
    with open(CHAT_FILE,"w") as file:
        file.write(chat)
    messagebox.showinfo(
        "Success",
        "Chat saved successfully!"
    )
def ask_ai():
    question = question_entry.get("1.0", tk.END).strip()

    if question == "":
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, "Please enter a question.")
        return
    
    response_box.insert(tk.END, "\nThinking...\n")
    window.update()

    

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content
        response_box.insert(tk.END, "\n")
        response_box.insert(tk.END, "You: " + question + "\n\n")
        response_box.insert(tk.END, "AI: " + answer)
        response_box.insert(tk.END, "\n")
        response_box.insert(tk.END, "-" * 60)
        response_box.insert(tk.END, "\n\n")

    except Exception as e:
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, f"Error:\n\n{e}")


window = tk.Tk()
window.title("🤖 AI Study Assistant")
window.geometry("700x600")
window.config(bg="#EAF4FF")


title = tk.Label(
    window,
    text="🤖 AI Study Assistant",
    font=("Arial", 18, "bold"),
    bg="#EAF4FF"
)
title.pack(pady=10)


tk.Label(
    window,
    text="Ask your question",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
).pack()


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
exit_button = tk.Button(window, text="Exit", command=exit_app, 
                            bg="red", fg="white", font=("Arial", 12, "bold"))
exit_button.pack(pady=50)

tk.Label(
    window,
    text="AI Response",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
).pack()


response_box = tk.Text(
    window,
    width=70,
    height=15,
    font=("Arial", 11),
    wrap="word"
)
response_box.pack(pady=10)



window.mainloop()
