from pydantic import BaseModel
from typing import Optional

class OpsBlogs(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]