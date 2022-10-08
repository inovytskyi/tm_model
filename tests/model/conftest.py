from pathlib import Path
from typing import List

import pytest
import yaml

from model.cf_config import CustomFieldConfig
from model.custom_field import CustomField
from model.step import Step
from model.test_case import TestCase


def load_cf_config(name: str) -> List[CustomFieldConfig]:
    cfile = Path('model') / 'configs' / name

    with cfile.open() as f:
        raw_config = yaml.load(f, Loader=yaml.SafeLoader)

    config = [CustomFieldConfig(**field) for field in raw_config["fields"]]
    return config


@pytest.fixture(scope="session")
def custom_field_config():
    return load_cf_config("cf_config.yaml")


