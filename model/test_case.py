from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel, validator, PydanticValueError

from model.cf_config import CustomFieldConfig
from model.custom_field import CustomField
from model.step import Step


def load_config() -> List[CustomFieldConfig]:
    cfile = Path('configs') / "custom_fields.yaml"

    with cfile.open() as f:
        raw_config = yaml.load(f, Loader=yaml.SafeLoader)

    config = [CustomFieldConfig(**field) for field in raw_config["fields"]]
    return config


class CustomFieldNameError(PydanticValueError):
    code = 'CustomFieldName'
    msg_template = 'Custom field "{field_name}" is not in configs. Available options is: {supported}.'


class CustomFieldValueError(PydanticValueError):
    code = 'CustomFieldValue'
    msg_template = 'Custom field "{field_name}" has unsupported value "{value}". Available options is: {supported}.'


class TestCase(BaseModel):
    id: int
    prefix: str
    summary: str
    steps: List[Step]
    cfg: List[CustomFieldConfig]
    custom_fields: List[CustomField]

    @validator('custom_fields')
    def fields_must_be_in_config(cls, v, values):
        for f in v:
            supported_fields = [field.name for field in values["cfg"]]
            if f.name not in supported_fields:
                raise CustomFieldNameError(field_name=f.name, supported=supported_fields)
            supported_values = [field.optional_values for field in values["cfg"] if field.name == f.name][0]
            if f.value not in supported_values:
                raise CustomFieldValueError(field_name=f.name, value=f.value, supported=supported_values)
        return v
