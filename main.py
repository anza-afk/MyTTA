from fastapi import APIRouter, FastAPI

app = FastAPI(title="MyTTA")

api_router = APIRouter()


@app.get('/')
async def index():
    return {'message': 'mytta main app'}

app.include_router(api_router)