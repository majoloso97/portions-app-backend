import os
from pydantic import BaseSettings

class Settings(BaseSettings):
  MONGODB_CONNECTIONSTRING: str


is_prod = os.getenv("IS_PROD")

settings = Settings(_env_file=str(object()) if is_prod else ".env")