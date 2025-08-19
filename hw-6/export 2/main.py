from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/v1/chat/completions")
def chat_completions():
    # Respuesta mock simple
    return JSONResponse(content={"id": "mock-id", "object": "chat.completion", "choices": [{"message": {"role": "assistant", "content": "Hola, soy un mock!"}}]})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 