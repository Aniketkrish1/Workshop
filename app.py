import streamlit as st
import cohere

# Initialize the Cohere client with your API key
API_KEY = 'ts9WtKV5SkVD4K3izWV8idxNeaoBykiT7zJkTQbY'  # Replace with your actual API key
co = cohere.Client(API_KEY)

# Streamlit app setup
st.title("Text Summarization App")
st.subheader("Enter text to summarize using Cohere")

# Input text area
input_text = st.text_area("Paste your text here:", height=200)

# Dropdown for summary length
length = st.selectbox(
    "Select summary length:",
    options=["short", "medium", "long"],
    index=0
)

# Dropdown for output format
format_option = st.selectbox(
    "Select output format:",
    options=["paragraph", "bullet"],
    index=0
)

# Button to trigger summarization
if st.button("Summarize Text"):
    if input_text.strip():
        # Call Cohere's summarize API
        try:
            response = co.summarize(
                text=input_text,
                length=length,
                format=format_option,
                model='summarize-xlarge'
            )
            st.subheader("Summarized Text:")
            st.write(response.summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown("Powered by [Cohere](https://cohere.com) and [Streamlit](https://streamlit.io)")
