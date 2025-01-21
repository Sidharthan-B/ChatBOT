from fastapi import FastAPI
from backend.database import setup_knowledge_base, query_knowledge_base
from backend.reminder import schedule_reminder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Chatbot backend is running"}

@app.post("/query/")
async def query(user_query: str):
    try:
        response = query_knowledge_base(user_query)
        return {"response": response}
    except Exception as e:
        return {"error": f"Error processing the query: {str(e)}"}

@app.post("/reminder/")
async def reminder(message: str, time: str):
    try:
        schedule_reminder(message, time)
        return {"status": "Reminder set"}
    except Exception as e:
        return {"error": f"Error setting the reminder: {str(e)}"}
