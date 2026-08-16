# 📚 Offline AI Study Assistant

An offline AI-powered study assistant that helps students understand academic topics by asking questions and receiving AI-generated answers.

The application runs locally using **Ollama** and the **Qwen3 1.7B** language model, with a simple web interface built using **Flask**.

---

## 🚀 Project Overview

**Offline AI Study Assistant** is designed for students who want to study without depending on an internet-based AI service.

A student can enter any academic question and choose how they want the answer:

* **Simple Answer** — short and easy explanation
* **Detailed Explanation** — complete teaching-style explanation
* **Exam Answer** — structured answer suitable for exam preparation

The AI generates the answer locally through Ollama.

---

## ✨ Features

* 🤖 Local AI-powered question answering
* 📚 Ask questions from different academic topics
* 📝 Simple Answer mode
* 📖 Detailed Explanation mode
* 🎯 Exam Answer mode
* 📋 Copy Answer button
* 🔄 New Question button
* ✨ Markdown-formatted AI responses
* ⌨️ `Ctrl + Enter` shortcut to submit a question
* 🔒 No external AI API key required
* 💻 Runs locally on the user's computer

---

## 🧠 How It Works

The application follows this basic workflow:

```text
Student Question
       ↓
Flask Web Application
       ↓
Prompt Generation
       ↓
Ollama
       ↓
Qwen3 1.7B Model
       ↓
AI Generated Answer
       ↓
Formatted Answer in Browser
```

The Flask application sends the student's question to the locally running Ollama server.

Ollama processes the question using the **Qwen3 1.7B** model and returns the generated response.

The response is then displayed in the browser using Markdown formatting.

---

## 🎓 Answer Modes

### 1. Simple Answer

Provides a short and easy-to-understand explanation.

Useful when the student needs a quick answer.

### 2. Detailed Explanation

Provides a deeper explanation of the topic.

Depending on the question, the answer can include:

* Definition
* Key concepts
* How it works
* Types
* Examples
* Real-world applications
* Advantages and limitations
* Conclusion

This mode is designed for students who want to properly understand a topic.

### 3. Exam Answer

Provides a structured answer focused on exam preparation.

It can include:

* Definition
* Important points
* Headings
* Examples
* Organized explanations

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Requests**
* **Ollama**
* **Qwen3 1.7B**
* **HTML**
* **CSS**
* **JavaScript**
* **Marked.js**

---

## 📁 Project Structure

```text
offline question solve app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── .venv/
```

> `.venv/` is used only for the local Python environment and is excluded from GitHub using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd offline-question-solve-app
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

---

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Install Ollama on your computer and make sure it is available from the terminal.

Check the installation:

```bash
ollama --version
```

---

## 📥 Download the Qwen3 Model

Run:

```bash
ollama pull qwen3:1.7b
```

After downloading, the model can be tested with:

```bash
ollama run qwen3:1.7b
```

---

## ▶️ Run the Application

First make sure Ollama is running.

Then activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Run Flask:

```bash
python app.py
```

The application will start locally.

Open the URL shown by Flask in your browser, usually:

```text
http://127.0.0.1:5000
```

---

## 💡 Example Questions

You can ask questions such as:

```text
What is Machine Learning?
```

```text
What is Python?
```

```text
Explain DBMS.
```

```text
What is Newton's Second Law?
```

```text
Explain Operating System.
```

The answer will change according to the question and the selected answer mode.

---

## 🔐 Privacy

The AI model runs locally through Ollama.

The student's question is sent to the locally running Ollama service rather than to an external AI API.

No OpenAI API key or other cloud AI API key is required for the current version.

---

## 🚧 Future Improvements

Possible future improvements include:

* 📄 PDF and document-based question answering
* 📚 Subject-wise study sections
* 🧠 Conversation history
* 💾 Save important answers
* 🔊 Text-to-speech
* 🌙 Dark mode
* 📱 Improved mobile interface
* 📊 Study progress tracking
* 🔍 Search previous questions
* 📝 Automatic quiz generation
* 📖 Notes generation from topics

---

## 👨‍💻 Author

**Ankit Singh**

This project was created as an AI/ML learning project to explore local AI models, Flask web applications, and AI-powered educational tools.
