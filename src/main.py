from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pipeline.producer.producer_router import producer_route

app = FastAPI()
app.include_router(producer_route)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)