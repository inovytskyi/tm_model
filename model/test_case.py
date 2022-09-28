from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel, validator, PydanticValueError

from model.cf_config import CustomFields
from model.custom_field import CustomField
from model.step import Step


def load_config() -> CustomFields:
    cfile = Path('configs') / "custom_fields.yaml"

    with cfile.open() as f:
        raw_config = yaml.load(f, Loader=yaml.SafeLoader)

    config = CustomFields(**raw_config)
    return config


class CustomFieldNameError(PydanticValueError):
    code = 'CustomFieldName'
    msg_template = 'Custom field "{field_name}" is not in config. Available options is: {supported}.'


class CustomFieldValueError(PydanticValueError):
    code = 'CustomFieldValue'
    msg_template = 'Custom field "{field_name}" has unsupported value "{value}". Available options is: {supported}.'

class TestCase(BaseModel):
    id: int
    prefix: str
    summary: str
    steps: List[Step]
    custom_fields: List[CustomField]

    @validator('custom_fields')
    def fields_must_be_in_config(cls, values):
        cfg = load_config()
        for v in values:
            supported_fields = [field.name for field in cfg.fields]
            if v.name not in supported_fields:
                raise CustomFieldNameError(field_name=v.name, supported=supported_fields)
            supported_values = [field.optional_values for field in cfg.fields if field.name == v.name][0]
            if v.value not in supported_values:
                raise CustomFieldValueError(field_name=v.name, value=v.value, supported=supported_values)
        return values


