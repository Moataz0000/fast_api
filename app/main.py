from fastapi import FastAPI
from enum import Enum
from app.routes import router

app = FastAPI()



app.include_router(router)

@app.get('/')
async def root():
    return {'message': 'Welcom to my FastAPI project!'}


