from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import GitbookLoader
 
 #Load the documents from the Gitbook
#loader = GitbookLoader("https://new-native.gitbook.io/onboarding/")
#docs = loader.load()
#Any other document loader can be used here

#Run the summarization chain
chain = load_summarize_chain(llm, chain_type="map_reduce")
docs2 =chain.run(docs)
print(docs2)