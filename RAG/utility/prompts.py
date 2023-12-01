def prompt_template(question, context):
    auto_prompt = f"""
    <s>[INST] <<SYS>>
    You are a helpful assistant who answers from the information mentioned in the context.
    
    Only answer from the given context be it right or wrong.
    <</SYS>>
    Question: {question}
    Context: 
    {context} [/INST]
    """
    return auto_prompt
