from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException

load_dotenv()
app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("./index.html")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
)
class Query(BaseModel):
    query: str

@app.post("/query")
async def process_query(query: Query) -> Dict[str, str]:
    messages = [
        ("system", "You are a helpful and natural-sounding voice assistant. Respond in clear and conversational language without special characters or formatting. Keep responses concise, engaging, and easy to understand for text-to-speech conversion."),
        ("human", query.query),
    ]
    response = ""
    try:
        for chunk in llm.stream(messages):
            response += str(chunk.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
    
    return {"response": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0000", port=3000)

