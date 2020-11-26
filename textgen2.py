import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen

st.title("AITEXTGEN Web App")

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 
#prompt_text = "Python is awesome"
prompt_text = st.text_input(label = "Enter your prompt text...",
            value = "Computer is beautiful")

with st.spinner("AI is at Work........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 100 )
st.success("AI Successfully generated the below text ")
st.balloons()
# print ai generated text
print(gpt_text)

st.text(gpt_text)
