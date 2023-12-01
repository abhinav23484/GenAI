from inference.load_llm import LLMObj
from utility.prompts import prompt_template
from inference.retriever import get_documents


def generate_output(question):
    """Loading Initial Objects and getting output from LLM"""
    documents = get_documents(query=question)
    prompt = prompt_template(question=question, context=documents)
    client = LLMObj()
    # return client(prompt)
    for tokens in client(prompt):
        yield f"{tokens}"
