# GenAI
*Implementations of LLMs for different use cases*

I divide RAG pipelines to be a three step process - 1.) Chunking 2.)Vectordb and persistence 3.) Output Generation  \
Creating right chunks for specific use cases is the most important part in getting accurate answers. Work is required around this part. To persist data we are using sqlitedb. Other databases like in-memory or Postgresql can also be used. For indexing the vectors and performing vector search we are using faiss db. We can also use different sentence transformers model to see the difference in accuracy according to our use case.
