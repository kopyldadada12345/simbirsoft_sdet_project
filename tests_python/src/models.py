

from pydantic import BaseModel
from typing import List


class AdditionRequest(BaseModel):
    additional_info: str
    additional_number: int


class AdditionResponse(AdditionRequest):
    id: int


class EntityRequest(BaseModel):
    title: str
    verified: bool
    important_numbers: List[int]
    addition: AdditionRequest


class Entity(BaseModel):
    id: int
    title: str
    verified: bool
    important_numbers: List[int]
    addition: AdditionResponse


#new
class EntitiesResponse(BaseModel):
    entity: List[Entity]