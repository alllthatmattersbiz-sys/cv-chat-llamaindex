import streamlit as st

from llama_index.core import VectorStoreIndex, Settings, Document
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import fitz  # PyMuPDF


# ---------------------------
# PDF Loader
# ---------------------------
def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# ---------------------------
# UI
# ---------------------------
st.title("📄 Chat with Your CV (LlamaIndex Framework)")

uploaded_file = st.file_uploader("Upload your CV (PDF)", type="pdf")


# ---------------------------
# Setup Models
# ---------------------------
Settings.llm = Anthropic(
    model="claude-haiku-4-5-20251001"
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en"
)


# ---------------------------
# Main App
# ---------------------------
if uploaded_file is not None:

    # Save file locally
    with open("cv.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text
    text = load_pdf("cv.pdf")

    # Debug (optional)
    st.write("Preview of extracted text:")
    st.write(text[:1000])

    # Convert to document
    documents = [Document(text=text)]

    # Create index
    index = VectorStoreIndex.from_documents(documents)

    # Query engine
    query_engine = index.as_query_engine()

    # Ask question
    question = st.text_input(
        "Ask a question about the CV, e.g. 'What is the candidate's experience with Python?'"
    )

    if question:
        response = query_engine.query(question)
        st.write(response.response)