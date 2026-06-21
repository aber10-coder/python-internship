import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from db import init_db
from routers import auth_router, tasks_router

security = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Secure Task API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = round((time.time() - start) * 1000, 2)
    print(f"{request.method} {request.url.path} → {response.status_code} ({duration}ms)")
    return response

app.include_router(auth_router.router)
app.include_router(tasks_router.router)