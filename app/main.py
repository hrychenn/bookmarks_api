from fastapi import FastAPI
app = FastAPI(title="Bookmarks API", version="1.0.0")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
