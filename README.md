# Pretrained Support ChatBot

An AI chatbot trained on PDFs to provide smart and accurate answers based on document content.

## ✨ Features

- 💬 Conversational memory with context awareness
- 📄 PDF ingestion and chunk-based retrieval
- 🔎 Local vector search using FAISS
- 🧠 Powered by HuggingFace LLMs (e.g., flan-t5-xxl)
- 🎛️ Simple UI built with Streamlit

## 🧪 Tech Stack

- Python 3.9
- Streamlit
- LangChain
- HuggingFaceHub
- FAISS
- Instructor Embeddings (`hkunlp/instructor-xl`)

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/pretrained-support-chatbot.git
cd pretrained-support-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your PDF to the training_data/ folder.

4. Set your HuggingFace/Any other service API token:

5. Run the app:
```bash
streamlit run main.py
```
## 📁 File Structure
```css
├── main.py
├── utils.py
├── retriever.py
├── FAISS_compatibility.py
├── templates/
│   ├── streamlit_template.py
│   └── html_template.py
├── training_data/
│   └── your_pdf.pdf
├── requirements.txt
└── README.md
```
## ⚠️ Limitations

- Only one PDF is supported at a time

- Manual API key setup required

- Not yet deployed on the cloud

## 👤 Author
Gabriel Guerra

### This project is open for anyone to use or modify.