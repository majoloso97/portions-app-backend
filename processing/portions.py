from models.Portion import Portion
from scrapper.Scrapper import Scrapper

async def update_portions_data():
  await Portion.delete_all()

  sc = Scrapper()
  data = sc.get_processed_data()

  docs = []
  for item in data:
    docs.append(Portion(**item))

  await Portion.insert_many(docs)


async def get_food_data(food: str):
  portion = await Portion.find_one(Portion.Alimento == food)

  return portion

