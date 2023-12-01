from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import faiss
from sqlalchemy import create_engine

embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
engine = create_engine("sqlite:///%s" % "D:\\Git_Workspace\\GenAI\\RAG\\vectorstoredb\\data.db")


def get_documents(query):
    """Fetching the most relevant document to be passed to the LLM"""
    index_file = "./vectorstoredb/data.index"  # Loading Index file
    _query = embedder.encode(query)  # Converting to query to search vector
    _query_vector = np.array([_query])
    # faiss.normalize_L2(_query)
    index = faiss.read_index(index_file)  # Loading Index from file
    top_k = 3  # Loading the most relevant document
    distance, ann = index.search(_query_vector, k=top_k)  # Performing an index search
    results = pd.DataFrame({'distance': distance[0], 'ann': ann[0]})
    df = pd.read_sql("contents", engine)
    pd.merge(results, df, left_on='ann', right_index=True)
    value_label = df['context']
    chunk = value_label[ann[0][0]]
    return chunk

