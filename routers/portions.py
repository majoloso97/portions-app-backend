from processing import portions
from fastapi import APIRouter, Body

router = APIRouter(prefix='/portions')

@router.get('/load_portions/')
async def root():
  await portions.update_portions_data()
    
  return {"message": "Data is imported"}


@router.get('/get-food-data/')
async def get_food(food: str = Body(min_length=1)):
  food_data = await portions.get_food_data(food)

  if not food_data is None:
    return food_data
  
  return {'message': 'Food not found'}