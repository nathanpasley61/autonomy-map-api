
from fastapi import FastAPI

app = FastAPI(title="Autonomy Map API")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "autonomy-map-api"}
