import streamlit as st
import ollama

st.set_page_config(page_title="Ollama Streamlit Chatbot")

st.title("Local LLM Chatbot with Ollama")

# Initialize chat history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Replace 'llama2' with the model you have pulled in Ollama (e.g., 'mistral', 'llama3')
                response = ollama.chat(model='deepseek-r1:1.5b', messages=[
                    {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                ])
                assistant_response = response['message']['content']
                st.markdown(assistant_response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                st.error(f"Error communicating with Ollama: {e}")
                st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})
