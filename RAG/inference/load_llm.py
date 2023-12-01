from ctransformers import AutoModelForCausalLM


def LLMObj():
    """"""
    client = AutoModelForCausalLM.from_pretrained(
        "../../../../LLM_Models/llama-2-7b-chat.ggmlv3.q4_1.bin",
        model_type="llama",
        temperature=0.05,
        top_k=40,
        top_p=0.95,
        repetition_penalty=1.1,
        last_n_tokens=64,
        seed=-1,
        max_new_tokens=256,
        stop=None,
        stream=True,
        reset=True,
        batch_size=8,
        threads=-1,
        context_length=1024,
        gpu_layers=5
    )
    return client
