from fastapi import FastAPI
import uvicorn
from src.routes.router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Fast API Project",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True, env_file=".env")
