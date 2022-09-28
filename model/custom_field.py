from typing import Any
from pydantic import BaseModel


class CustomField(BaseModel):
    name: str
    value: Any
