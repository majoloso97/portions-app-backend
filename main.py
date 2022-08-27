from fastapi import FastAPI, Body
from events import start_handler
from routers import portions

app = FastAPI()

app.add_event_handler('startup', start_handler(app))
app.include_router(portions.router)

