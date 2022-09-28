from typing import Optional, List
from pydantic import BaseSettings, BaseModel


class CustomFieldConfig(BaseModel):
    name: str
    optional_values: Optional[List]


class CustomFields(BaseSettings):
    fields: List[CustomFieldConfig]

