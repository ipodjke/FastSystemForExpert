from fastapi import FastAPI

import db

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
async def read_root():
    return await db.User.objects.all()


@app.on_event("startup")
async def startup():
    if not db.database.is_connected:
        await db.database.connect()
    await db.User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if db.database.is_connected:
        await db.database.disconnect()
