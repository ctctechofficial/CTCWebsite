from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="CTC Tech - CodeToCareer", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get("/api/health")
def health():
    return {"status": "ok", "brand": "CTC Tech - CodeToCareer"}

@app.get("/", include_in_schema=False)
def home():
    return FileResponse(BASE_DIR / "templates" / "index.html")

BASE_DIR = Path(__file__).resolve().parent

@app.get("/googlef644425f8a684ee4.html")
def google_verification():
    file_path = BASE_DIR / "googlef644425f8a684ee4.html"
    return FileResponse(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
