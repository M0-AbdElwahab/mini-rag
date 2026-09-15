from pydantic import BaseModel, Field, validator  # type: ignore[import-not-found]
from typing import Optional
from bson.objectid import ObjectId  # type: ignore[import-not-found]

class DataChunk(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    

    class Config:
        arbitrary_types_allowed = True