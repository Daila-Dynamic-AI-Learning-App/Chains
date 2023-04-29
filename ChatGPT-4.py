import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#write openai api key as an os environment variable
import os
apikey = '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'
os.environ["OPENAI_API_KEY"] = apikey

st.title("ChatGPT 4")
prompt = st.text_area("Enter text here your question", height=200)


LLM = OpenAI(temperature=0.9)

#show stuff in the screen if there is a prompt
if prompt:
    response = LLM(prompt)
    st.write("GPT4 is thinking..")
    st.write(response)



