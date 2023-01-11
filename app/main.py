from fastapi import FastAPI
from app.events import start_handler
from app.api.v1.portions import portions

app = FastAPI()

app.add_event_handler('startup', start_handler(app))
app.include_router(portions.router)
