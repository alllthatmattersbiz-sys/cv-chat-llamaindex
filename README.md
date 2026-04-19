
# 📄 CV Chat Assistant using LlamaIndex

An AI-powered Streamlit application that allows users to upload a CV (PDF) and interactively ask questions about its content using a Retrieval-Augmented Generation (RAG) pipeline built with **LlamaIndex**.

---

## 🚀 Demo

Upload a CV and ask questions like:
- What is the candidate’s experience with Python?
- What projects has the candidate worked on?
- What skills are mentioned in the CV?

---

## 🧠 Architecture Overview

This project uses a simple RAG pipeline:

1. **PDF Parsing** → Extract text from CV using PyMuPDF  
2. **Embedding Generation** → Convert text into embeddings using HuggingFace (`bge-small-en`)  
3. **Vector Indexing** → Store embeddings using LlamaIndex `VectorStoreIndex`  
4. **Query Engine** → Retrieve relevant context and generate answers using Anthropic LLM  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LlamaIndex  
- Anthropic Claude (Haiku model)  
- HuggingFace Embeddings (`BAAI/bge-small-en`)  
- PyMuPDF (fitz)  

---

## 📁 Project Structure

```

cv-chat-llamaindex/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── .gitignore            # Ignored files (venv, env, etc.)

````

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/alllthatmattersbiz-sys/cv-chat-llamaindex.git
cd cv-chat-llamaindex
````

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Anthropic API key:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Key Features

* Upload CV in PDF format
* Ask natural language questions about the CV
* Semantic search over CV content using embeddings
* Fast response using Claude Haiku model
* RAG-based architecture using LlamaIndex

---

## 📌 Example Use Cases

* HR screening automation
* Personal CV analysis tool
* Recruitment assistant prototype
* Learning RAG pipelines with LLMs

---

## 📈 Future Improvements

* Add multi-CV comparison feature
* Store embeddings persistently (FAISS / Chroma)
* Add chat history memory
* Support DOCX and LinkedIn parsing
* Deploy on Streamlit Cloud / AWS

---

## ⚠️ Notes

* Do NOT upload `venv/` or `.env` to GitHub
* Ensure API keys are stored securely
* This project is for educational and prototyping purposes

---

## 👨‍💻 Author

Built as a personal project to explore:

* Retrieval-Augmented Generation (RAG)
* LlamaIndex framework
* LLM-based document intelligence systems

```

---

If you want, I can next help you:
- :contentReference[oaicite:0]{index=0}
- or :contentReference[oaicite:1]{index=1}
```
