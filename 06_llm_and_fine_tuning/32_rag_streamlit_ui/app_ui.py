import streamlit as st
import requests

# Title
st.title("RAG AI Assistant 🤖")

# Input box
query = st.text_input("Enter your question:")

# Button click
if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(
                "https://rag-api-nxgf.onrender.com/ask",
                json={"query": query}
            )
            
            data = response.json()
            
            # Display output
            st.subheader("Answer")
            st.write(data["answer"])
            
            st.subheader("Confidence")
            st.write(data["confidence"])
            
            # Optional fields
            if data.get("tool_output"):
                st.subheader("Tool Output")
                st.write(data["tool_output"])
                
        except Exception as e:
            st.error("Error connecting to API. Make sure FastAPI server is running.")
