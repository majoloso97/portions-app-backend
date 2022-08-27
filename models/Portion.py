from typing import Optional
from beanie import Document, Indexed
import pymongo

class Portion(Document):
  Alimento: Indexed(str, index_type = pymongo.TEXT)
  Grupo: str
  Porción: str
  taza: Optional[float] = None
  gramo: Optional[float] = None
  oz: Optional[float] = None
  unidad: Optional[float] = None
  clara: Optional[float] = None
  cda: Optional[float] = None
  ml: Optional[float] = None
  cdita: Optional[float] = None

  class Settings: 
    name = 'Portions'