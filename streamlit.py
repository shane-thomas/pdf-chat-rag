import streamlit as st
import app as main

st.title("Chat with PDFs 📚 ")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type="pdf",
    accept_multiple_files=False
)

if uploaded_file:
    main.upload_pdf(uploaded_file)
    db = main.create_vector_store(main.pdfs_directory + uploaded_file.name)
    question = st.chat_input()

    if question:
        st.chat_message("user").write(question)
        related_documents = main.retrieve_docs(db, question)
        answer = main.question_pdf(question, related_documents)
        st.chat_message("assistant").write(answer)
