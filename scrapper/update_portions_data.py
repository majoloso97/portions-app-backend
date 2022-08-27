from beanie import init_beanie
import motor.motor_asyncio
from models.Portion import Portion
from scrapper.Scrapper import Scrapper

async def init():
  # Crete Motor client
  client = motor.motor_asyncio.AsyncIOMotorClient(
      "mongodb+srv://admin:p6QIGaLdRjMufzqL@mainportionsdb.ut5blzp.mongodb.net/?retryWrites=true&w=majority"
  )

  # Init beanie with the Portion document class and a database
  await init_beanie(database=client.MainPortionsDB, document_models=[Portion])


async def update_portions_data():
  await init()

  await Portion.delete_all()

  sc = Scrapper()
  data = sc.get_processed_data()

  docs = []
  for item in data:
    docs.append(Portion(**item))

  await Portion.insert_many(docs)


async def get_food_data(food: str):
  await init()

  portion = await Portion.find_one(Portion.Alimento == food)

  return portion


# asyncio.run(update_portions_data())