# imports
import nltk
import os
from pypdf import PdfReader
from docx import Document
from add_to_kb import persist_data

# Initialize tokenizer
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")


def extract_data(filepath):
    """Extract data from file based on the file type"""
    head, filename = os.path.split(filepath)  # Getting filename from filepath
    # initialize a text string to store all data from all pages under a single string
    all_pages = ""
    if filename.endswith(".pdf"):  # process pdf files
        reader = PdfReader(filepath)
        for page in reader.pages:
            text = page.extract_text()
            all_pages = all_pages + text

    elif filename.endswith(".docx"):   # process doc files
        doc = Document(filepath)
        for para in doc.paragraphs:
            all_pages = all_pages + para.text
    else:
        return "File Type Not Supported Yet"

    # Create chunks after extraction is complete
    create_chunks(filename, all_pages)


def create_chunks(filename, data):
    """Method to parse the data and create chunks"""
    tokenized_data = tokenizer.tokenize(data)
    token_stash = ""
    tokens_list = []
    document_number = 0
    for tokens in tokenized_data:
        num_tokens = len(tokens.split())
        token_stash = token_stash + tokens
        # Create chunks of the desired size but with complete sentences
        if len(token_stash.split()) > 512:
            tokens_list.append([token_stash, filename+"_"+str(document_number)])  # Assign a document name to each chunk
            token_stash = ""
            document_number = document_number + 1

    persist_data(tokens_list)


extract_data("../datasets/bitcoin.pdf")
