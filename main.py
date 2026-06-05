from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.routes.chatRoute import router as chatRouter
app= FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"] )

@app.get("/")
async def root():
    return {"status":"ok"}

app.include_router(chatRouter,prefix="/api/v1/chat")