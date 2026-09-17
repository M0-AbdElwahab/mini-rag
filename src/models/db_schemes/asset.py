try:
    from pydantic import BaseModel, Field, field_validator  # type: ignore[import-not-found]
    validator = field_validator
except ImportError:  # pragma: no cover
    from pydantic import BaseModel, Field, validator  # type: ignore[import-not-found]


from typing import Optional
from datetime import datetime

try:
    from bson.objectid import ObjectId  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    class ObjectId(str):
        """Fallback for environments without bson installed."""





class Asset(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    asset_project_id: ObjectId
    asset_type: str = Field(..., min_length=1)
    asset_name: str = Field(..., min_length=1)
    asset_size: int = Field(ge=0, default=None)
    asset_config: dict = Field(default=None)
    asset_pushed_at: datetime = Field(default=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):

        return [
            {
                "key": [
                    ("asset_project_id", 1)
                ],
                "name": "asset_project_id_index_1",
                "unique": False
            },
            {
                "key": [
                    ("asset_project_id", 1),
                    ("asset_name", 1)
                ],
                "name": "asset_project_id_name_index_1",
                "unique": True
            },
        ]