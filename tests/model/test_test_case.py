import pytest
from pydantic import ValidationError

from model.custom_field import CustomField
from model.step import Step
from model.test_case import TestCase, CustomFieldNameError


def test_creation_test_case_incorrect_field_name(custom_field_config):
    steps = [Step(action="Press button", expected_result="Popup window is opened"),
             Step(action="Press close button", expected_result="Popup window is closed")]
    custom_fields = [CustomField(name="bran", value="SOP"),
                     CustomField(name="type", value="functional")]

    with pytest.raises(ValidationError) as exception:
        test_case = TestCase(cfg=custom_field_config, id=1, summary="First test case", prefix="MSP", steps=steps,
                             custom_fields=custom_fields)


def test_creation_test_case_incorrect_field_value(custom_field_config):
    steps = [Step(action="Press button", expected_result="Popup window is opened"),
             Step(action="Press close button", expected_result="Popup window is closed")]
    custom_fields = [CustomField(name="branch", value="SUP"),
                     CustomField(name="type", value="functional")]

    with pytest.raises(ValidationError) as exception:
        test_case = TestCase(cfg=custom_field_config, id=1, summary="First test case", prefix="MSP", steps=steps,
                             custom_fields=custom_fields)


def test_creation_test_case_correct_fields(custom_field_config):
    steps = [Step(action="Press button", expected_result="Popup window is opened"),
             Step(action="Press close button", expected_result="Popup window is closed")]
    custom_fields = [CustomField(name="branch", value="SOP"),
                     CustomField(name="type", value="functional")]

    try:
        TestCase(cfg=custom_field_config, id=1, summary="First test case", prefix="MSP", steps=steps,
                 custom_fields=custom_fields)
    except ValidationError as err:
        assert False, f"Exception was raised: {err}"
