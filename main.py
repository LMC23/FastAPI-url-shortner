import uvicorn
from db.supabase_db import client
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from schemas.url_schemas import CreateUrl, ShowCreateUrl
from utils.generate_key import generate_keys


app = FastAPI()


@app.get("/")
async def root():
    return {"welcome_message": "Welcome to the URL shortener API!"}


@app.post("/url")
async def create_url(url: CreateUrl) -> ShowCreateUrl:
    keys = generate_keys()
    param = {"clicks": 0, "is_active": True, "key": keys[1], "secret_key": keys[0], "target_url": url.target_url}

    data = client.table("url_table").insert(param).execute()
    return data.data[0]


@app.get("/{url_key}")
def test(url_key):
    try:
        data = client.table("url_table").select("*").eq("key", url_key).execute()
        target_url = data.data[0]["target_url"]
        return RedirectResponse(target_url)
    except:
        return HTTPException(status_code=404, detail="Item not found")


@app.get("/admin/{secret_key}")
def test(secret_key):
    return {"mesaj": "ok"}


@app.delete("/admin/{secret_key}")
def test(secret_key):
    return {"mesaj": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=3007, reload=True)
