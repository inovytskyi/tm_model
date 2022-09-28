from devtools import pprint

from model.step import Step
from model.custom_field import CustomField
from model.test_case import TestCase


def main() -> None:
    steps = [Step(action="Press button", expected_result="Popup window is opened"),
             Step(action="Press close button", expected_result="Popup window is closed")]
    custom_fields = [CustomField(name="branch", value="SOP"),
                     CustomField(name="type", value="functional")]

    test_case = TestCase(id=1, summary="First test case", prefix="MSP", steps=steps, custom_fields=custom_fields)
    pprint(test_case)



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
