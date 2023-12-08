# GenAI
*Implementations of LLMs for different use cases*

I divide RAG pipelines to be a three step process - 1.) Chunking 2.)Vectordb and persistence 3.) Output Generation  \
\
Creating right chunks for specific use cases is the most important part in getting accurate answers. Work is required around this part. To persist data we are using sqlitedb. Other databases like in-memory or Postgresql can also be used. For indexing the vectors and performing vector search we are using faiss db. We can also use different sentence transformers model to see the difference in accuracy according to our use case.

### RAG
For the project under RAG is a implenetation of the piepline with native python modules. This gives us a lot of control over our pipeline and prevents us from using any bloated python SDKs. Here we can clearly understand and control our chain and retrievals, set prompts easily, see the right chunk(context) of data being passed and modify those according to our needs.

##### GETTING STARTED
  Clone the repo. - git clone https://github.com/abhinav23484/GenAI.git \
  CD to RAG - CD RAG \
  Create an environment - python -m venv path-to-project_dir/GenAI/RAG/venv \
  Activate the environment - source venv/bin/activate \
  Install dependencies - pip install requirements.txt \
  Run it as an endpoint - uvicorn main:app --reload 

The endpoint can be tested at - http://127.0.0.1:8000/docs 

Example run - 
