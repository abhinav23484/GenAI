# imports
import faiss
import pandas as pd
from sqlalchemy import create_engine
from sentence_transformers import SentenceTransformer

# Load embeddings
# Model can be downloaded to local storge from huggingface and path to the directory can be provided here.
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

# Initializing db engine to persist data. Any db including in memory databases should work.
engine = create_engine("sqlite:///%s" % "D:\\Git_Workspace\\GenAI\\RAG\\vectorstoredb\\data.db")


def persist_data(data):
    """Persistence of training data to local file storage"""
    df = pd.DataFrame(data, columns=['context', 'doc_name'])
    df.to_sql(name="contents", con=engine, if_exists='append', index=False)  # Writing to sqldb
    df_load = pd.read_sql("contents", con=engine)  # Loading to check for duplicates
    df_load.drop_duplicates(inplace=True)  # Dropping Duplicates
    df_load.to_sql(name="contents", con=engine, if_exists='replace', index=False)  # Writing non duplicate data
    df_read = pd.read_sql("contents", con=engine)  # Finally loading non-duplicate data for embeddings creation
    add_vectostore(df_read)


def add_vectostore(df_db):
    print(df_db.head(100))
    # Index file
    index_file = "D:\\Git_Workspace\\GenAI\\RAG\\vectorstoredb\\data.index"
    corpus = df_db["context"]  # initialize corpus
    text_embeddings = embedder.encode(corpus)  # Create embeddings of data
    vector_dimension = text_embeddings.shape[1]  # Getting the vector dimension of embeddings created
    n_list = 2
    # Indexes so far have stored our vectors as full (eg Flat) vectors. Now, in very large datasets this can quickly
    # become a problem. Fortunately, Faiss comes with the ability to compress our vectors using Product Quantization
    # (PQ). PQ achieves this approximated similarity operation by compressing the vectors themselves, which consists
    # of three steps.
    quantizer = faiss.IndexFlatL2(vector_dimension)  # Defining quantizer to
    index = faiss.IndexIVFFlat(quantizer, vector_dimension, n_list, faiss.METRIC_L2)  # Initializing Indexes
    assert not index.is_trained  # Checking and training indexes
    index.train(text_embeddings)
    assert index.is_trained
    faiss.normalize_L2(text_embeddings)
    index.add(text_embeddings)
    faiss.write_index(index, index_file)



