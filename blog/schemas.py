from pydantic import BaseModel
from typing import Optional

class Blogs(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]