from app.services.portions import portions
from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/portions')

@router.get('/load_portions/')
async def root():
  await portions.update_portions_data()
    
  return {"message": "Data is imported"}


@router.get('/get-food-data/{food}')
async def get_food(food):
  food_data = await portions.get_food_data(food)

  if not food_data is None:
    return food_data
  
  return {'message': 'Food not found'}