from pydantic import BaseModel, Field  # type: ignore[import-not-found]
from typing import Optional

class ProcessRequest(BaseModel):
    File_id: str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset: Optional[int] = 0