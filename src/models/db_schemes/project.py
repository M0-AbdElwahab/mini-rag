try:
    from pydantic import BaseModel, Field, field_validator  # type: ignore[import-not-found]
    validator = field_validator
except ImportError:  # pragma: no cover
    from pydantic import BaseModel, Field, validator  # type: ignore[import-not-found]


from typing import Optional


try:
    from bson.objectid import ObjectId  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    class ObjectId(str):
        """Fallback for environments without bson installed."""


class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value

    class Config:
        arbitrary_types_allowed = True
        
