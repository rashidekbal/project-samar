from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.routes.chatRoute import router as chatRouter
from src.agent.workflow import init_workflow
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_workflow()
    yield
app= FastAPI(lifespan=lifespan)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"] )

@app.get("/")
async def root():
    return {"status":"ok"}

app.include_router(chatRouter,prefix="/api/v1/chat")