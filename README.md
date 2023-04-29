# Chains

## Summary Chain
This is a chain that takes documents from any type of document loader supported by langchain and uses MapReduce to separate long documets into several and summarize and the summarize all the summaries together.
Requiremets:
``` 
pip install langchain openai 
```
You will need an OpenAI API key

## ChatGPT4
This a chatGPT clone using streamlit, works with any model but is designed to be used with GPT4.
Requirements:
``` 
pip install langchain openai streamlit
```
You will need an OpenAI API key

## Rewritter
This is a tool designed to help you rewrite text but can be used in several ways modifying the prompt, it expects a variable to be enter by the user and the prompt  can be adjusted accordingly.
Example usecase:
````
prompt_template = "What is a good name for a company that makes {product}?"

llm = OpenAI(temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
llm_chain("colorful socks")
```

```
{'product': 'colorful socks', 'text': '\n\nSocktastic!'}
````


Requirement:
``` 
pip install langchain openai streamlit
```

You will need an OpenAI API key

## Web Searcher Agent

This is an Agent that searches the web, is able to look at different results, refelct and give a conclusive answer once it believes it has foung the answer, useful for questions of current events.
Requirements:

``` 
pip install langchain openai streamlit
```
You will need an OpenAI API key and a SerpAPI API key
