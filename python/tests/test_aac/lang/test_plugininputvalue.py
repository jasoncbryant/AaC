# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.plugininputvalue import PluginInputValue

TEST_DATA_ALL = {"name": "test", "value": "test"}

TEST_DATA_REQUIRED = {"name": "test", "value": "test"}


class TestPluginInputValue(unittest.TestCase):
    def test_plugininputvalue_from_dict_all_fields(self):
        plugininputvalue_dict = TEST_DATA_ALL
        instance = PluginInputValue.from_dict(deepcopy(plugininputvalue_dict))
        self.assertEqual(instance.name, plugininputvalue_dict["name"])
        self.assertEqual(instance.value, plugininputvalue_dict["value"])

        plugininputvalue_dict = TEST_DATA_REQUIRED
        instance = PluginInputValue.from_dict(deepcopy(plugininputvalue_dict))
        self.assertEqual(instance.name, plugininputvalue_dict["name"])
        self.assertEqual(instance.value, plugininputvalue_dict["value"])


if __name__ == "__main__":
    unittest.main()
