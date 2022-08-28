from fastapi import FastAPI, Body
from events import start_handler
from routers import portions
import uvicorn
import os

app = FastAPI()

app.add_event_handler('startup', start_handler(app))
app.include_router(portions.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=8000), log_level="info")