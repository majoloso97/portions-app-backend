from beanie import init_beanie
import motor.motor_asyncio
from config import settings
from models.Portion import Portion

async def initiate_database():
  # Crete Motor client
  client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_CONNECTIONSTRING)

  # Init beanie with the Portion document class and a database
  await init_beanie(database=client.MainPortionsDB, document_models=[Portion])