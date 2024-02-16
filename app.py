import os
from langchain.chains import LLMChain

if __name__ == "__main__":
    print("Hello I am LLM!")
    print(os.environ["OPENAPI_KEY"])
