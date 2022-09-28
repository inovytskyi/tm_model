from pydantic import BaseModel


class Step(BaseModel):
    action: str
    expected_result: str