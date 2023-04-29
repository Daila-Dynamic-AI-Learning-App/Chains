import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#write openai api key as an os environment variable
import os
apikey = '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'
os.environ["OPENAI_API_KEY"] = apikey

st.title("AI Rewritter Helper")
prompt = st.text_area("Enter text to be rewritten", height=200)

#Prompt template
Rewrite_Template = PromptTemplate(
    input_variables = ["input_text"],
    template = "Rewrite the following text {input_text}"
)


LLM = OpenAI(temperature=0.9)
rewrite_chain = LLMChain(llm=LLM, prompt = Rewrite_Template)

#sow stuff in the screen if there isa prompt
if prompt:
    response = rewrite_chain.run(input_text=prompt)
    st.write("AI Rewritting...")
    st.write(response)


