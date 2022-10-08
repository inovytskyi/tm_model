from pathlib import Path
from typing import List

import yaml
from devtools import pprint
from fastapi import FastAPI

from model.cf_config import CustomFieldConfig
from model.step import Step
from model.custom_field import CustomField
from model.test_case import TestCase


def load_config() -> List[CustomFieldConfig]:
    cfile = Path('configs') / "custom_fields.yaml"

    with cfile.open() as f:
        raw_config = yaml.load(f, Loader=yaml.SafeLoader)

    config = [CustomFieldConfig(**field) for field in raw_config["fields"]]
    return config


config = load_config()
app = FastAPI()


@app.get("/")
async def root():
    steps = [Step(action="Press button", expected_result="Popup window is opened"),
             Step(action="Press close button", expected_result="Popup window is closed")]
    custom_fields = [CustomField(name="branch", value="SOP"),
                     CustomField(name="type", value="functional")]

    test_case = TestCase(cfg=config, id=1, summary="First test case", prefix="MSP", steps=steps,
                         custom_fields=custom_fields)

    return test_case
