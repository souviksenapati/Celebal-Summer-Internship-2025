# 🤖 RAG Document Q&A Chatbot

A smart, interactive web application that enables users to upload documents and ask questions about their content using advanced RAG (Retrieval-Augmented Generation) technology. Built with Flask and powered by Groq's lightning-fast LLM inference.

---

# 🔗 Live Demo

   [Click here to try the project on Hugging Face 🚀](https://huggingface.co/spaces/souviksenapati/RAG_QA_ChatBot)

---

## ✨ Features

✅ **Multi-format Document Support**: PDF, DOCX, and TXT files  
✅ **Smart Document Replacement**: Each new upload replaces the previous document context  
✅ **Vector Similarity Search**: Custom vector store for relevant context retrieval  
✅ **Lightning-fast Inference**: Groq API with Llama3-8B model  
✅ **Modern Web Interface**: Drag-and-drop file upload with real-time chat  
✅ **Responsive Design**: Works seamlessly on desktop and mobile  
✅ **Real-time Processing**: Instant document processing and embedding generation  

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.10+
- Flask (Web Framework)
- Groq API (LLM Inference)
- SentenceTransformers (Text Embeddings)
- NumPy (Vector Operations)
- PyPDF2 (PDF Processing)
- python-docx (DOCX Processing)

**Frontend:**
- HTML5/CSS3
- Vanilla JavaScript
- Modern UI/UX Design
- Drag-and-Drop File Upload

**AI/ML:**
- RAG (Retrieval-Augmented Generation)
- all-MiniLM-L6-v2 (Embedding Model)
- Llama3-8B-8192 (Language Model via Groq)
- Custom Vector Store Implementation

**DevOps:**
- Docker Support
- Environment Configuration
- Secure File Handling

---

## ⚙️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/souviksenapati/Celebal-Summer-Internship-2025.git
cd Celebal-Summer-Internship-2025/Week_Assingments/Week_8
```

2. **Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
# Create .env file and add your Groq API key
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the application:**
```bash
python app.py
```

6. **Open your browser:**
```
http://localhost:7860
```

---

## 🚀 Usage

1. **Upload Document**: Drag and drop or click the 📎 button to upload PDF, DOCX, or TXT files
2. **Wait for Processing**: The system will extract text and generate embeddings
3. **Ask Questions**: Type your questions about the document content
4. **Get AI Responses**: Receive contextually relevant answers based on the document
5. **Upload New Document**: Each new upload replaces the previous document context

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Flask App     │    │   Groq API      │
│   (HTML/CSS/JS) │◄──►│   (Python)       │◄──►│   (Llama3-8B)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  Vector Store    │
                       │  (Embeddings)    │
                       └──────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │ SentenceTransf.  │
                       │ (all-MiniLM-L6)  │
                       └──────────────────┘
```

---

## 🐳 Docker Support

```bash
# Build the image
docker build -t rag-chatbot .

# Run the container
docker run -p 7860:7860 --env-file .env rag-chatbot
```

---

## 🤝 Contributing

Contributions are welcome! 🚀  

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Souvik Senapati**  
📧 Email: souviksenapati85@gmail.com  
🔗 LinkedIn: [linkedin.com/in/souviksenapati](https://linkedin.com/in/souviksenapati)  
🐙 GitHub: [github.com/souviksenapati](https://github.com/souviksenapati)

---

⭐ **Star this repository if you found it helpful!**