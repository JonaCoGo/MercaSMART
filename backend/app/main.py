from fastapi import FastAPI

app = FastAPI(title="MercaSMART API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a MercaSMART API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
