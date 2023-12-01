from inference.qa_chain import generate_output
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


class Paras(BaseModel):
    """Pydantic model for parameters"""
    query: str | None = None


app = FastAPI()


@app.post("/generate/")
async def generate(paras: Paras):
    """Generate response from LLM and stream it out at an endpoint"""
    query_string = paras.query
    # question = "What are the steps to run a bitcoin network?"
    # return generate_output(question=query_string)
    return StreamingResponse(generate_output(question=query_string), media_type="text/event-stream")

