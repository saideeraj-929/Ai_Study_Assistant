# 🤖 AI Study Assistant

An AI-powered desktop chatbot built using **Python**, **Tkinter**, and the **Groq API**.

This project allows users to ask questions through a graphical interface and receive AI-generated answers in real time.

---

## 📌 Features

* 🤖 Ask questions using AI
* 💬 Chat-style conversation interface
* 🧹 Clear Chat button
* 🚪 Exit confirmation dialog
* ⚡ Fast responses using Groq API
* 🛡 Error handling for API and network issues
* 🖥 Simple and clean Tkinter GUI

---

## 🛠 Technologies Used

* Python 3
* Tkinter
* Groq API
* Llama 3.3 70B Versatile Model

---

## 📂 Project Structure

AI-Study-Assistant/

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

└── screenshots/

---

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Study-Assistant.git
```

2. Install required packages

```bash
pip install -r requirements.txt
```

3. Set your Groq API Key

Windows Command Prompt

```cmd
set GROQ_API_KEY=your_api_key_here
```

Linux / macOS

```bash
export GROQ_API_KEY=your_api_key_here
```

4. Run the application

```bash
python main.py
```

---

## 📸 Screenshots

Add screenshots inside the **screenshots** folder.

Example:

* Home Screen
* AI Response
* Chat History

---

## 🔒 Security

The API key is **not stored in the source code**.

The application loads the key using environment variables:

```python
os.getenv("GROQ_API_KEY")
```

---

## 📈 Future Improvements

* Save Chat
* Export Chat as PDF
* Dark Mode
* Voice Input
* Voice Output
* Multiple AI Models
* Chat History
* Copy Response
* Markdown Support
* File Upload
* Image Analysis

---

## 👨‍💻 Author

**Sai Deeraj**

Diploma CSE Student

Learning Python, AI, Machine Learning, and Software Development.

GitHub: https://github.com/saideeraj-929

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
