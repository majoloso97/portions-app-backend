from typing import Callable
from fastapi import FastAPI
from database.config import initiate_database

def start_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await initiate_database()
        print("Starting DB!")

    return start_app