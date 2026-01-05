from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from query import get_local_ai_response # Importing the function we wrote earlier

app = FastAPI(title="The Digital Bistro AI API")

# Define the structure of the request
class ChatRequest(BaseModel):
    question: str

# Define the structure of the response
class ChatResponse(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"status": "The Digital Bistro API is online"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Run your existing local RAG logic
        ai_answer = get_local_ai_response(request.question)
        return ChatResponse(answer=ai_answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)