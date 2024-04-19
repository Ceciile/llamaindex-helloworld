import os
from dotenv import load_dotenv
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex

def main(url:str)-> None:
    """The module:attribute Python project."""
    docu = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=docu)
    query_eng = index.as_query_engine()
    response = query_eng.query("what's llama ?")
    print(response)
    
if __name__ == '__main__' :
    load_dotenv()
    if "OPENAI_API_KEY" not in os.environ:
        raise EnvironmentError("API_URL not set")
    API_URL = os.environ.get('OPENAI_API_KEY')

    print(f"OPEN_KEY is: ",API_URL)
    main(url='https://medium.com/@srgurupr/llm-ops-overview-part-1-b14a0d171d16')
    