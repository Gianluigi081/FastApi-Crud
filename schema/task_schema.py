from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    id: Optional[str]
    title: str
    description: str