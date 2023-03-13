from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'mytta main app'}