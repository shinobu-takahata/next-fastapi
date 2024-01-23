from fastapi import FastAPI
from api.routers import task, done
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()
# CORSを設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.jsアプリのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task.router)
app.include_router(done.router)

handler = Mangum(app)