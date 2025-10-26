# 🧠 Egyptian Arabic → English Translator

## Overview
This project provides a **complete translation pipeline** for converting **Egyptian Arabic** text into **English** using a fine-tuned Marian model from Hugging Face. It includes:
- A **FastAPI backend** for model inference.
- A **Streamlit frontend** for user interaction.
- A **Jupyter Notebook** for data exploration, preprocessing, or evaluation.

---

## ⚙️ Tech Stack
- **FastAPI** — lightweight and fast backend API.
- **Streamlit** — intuitive web UI for user interaction.
- **Hugging Face Transformers** — for translation model loading.
- **PyTorch** — model backend (uses GPU if available).

---

## 🧩 Project Structure
```
├── app/
│   ├── main.py              # FastAPI backend
│   └── translator.py        # Model loading and inference (optional split)
├── streamlit_app/
│   └── app.py               # Streamlit frontend
├── cleaned_github_ready_notebook.ipynb  # Notebook version
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/egyptian-arabic-translator.git
cd egyptian-arabic-translator
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI backend
```bash
uvicorn app.main:app --reload
```
➡️ API will start at: `http://127.0.0.1:8000`

### 5️⃣ Run the Streamlit frontend
```bash
streamlit run streamlit_app/app.py
```
➡️ Streamlit UI will open at: `http://localhost:8501`

---

## 🧠 Example Usage
**Input:**
> "إزيك يا صاحبي؟ عامل إيه؟"

**Output:**
> "How are you, my friend? How are you doing?"

---

## 🪄 Notes
- Ensure the FastAPI server is running **before launching Streamlit**.
- The model automatically uses GPU if available (`torch.cuda.is_available()`).
- To deploy, you can host the FastAPI API on Render or Hugging Face Spaces and Streamlit on Streamlit Cloud.

---
