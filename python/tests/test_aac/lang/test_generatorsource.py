# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.generatorsource import GeneratorSource

TEST_DATA_ALL = {
    "name": "test",
    "data_source": "test",
    "data_content": "test",
    "templates": [
        {
            "name": "test",
            "description": "test",
            "template_file": "test",
            "overwrite": "OVERWRITE",
            "helper_functions": [
                {
                    "name": "test",
                    "description": "test",
                    "package": "test",
                    "module": "test",
                    "function": "test",
                },
                {
                    "name": "test",
                    "description": "test",
                    "package": "test",
                    "module": "test",
                    "function": "test",
                },
            ],
            "output_target": "CODE",
            "output_path_uses_data_source_package": True,
            "output_file_prefix": "test",
            "output_file_name": "test",
            "output_file_suffix": "test",
            "output_file_extension": "test",
        },
        {
            "name": "test",
            "description": "test",
            "template_file": "test",
            "overwrite": "OVERWRITE",
            "helper_functions": [
                {
                    "name": "test",
                    "description": "test",
                    "package": "test",
                    "module": "test",
                    "function": "test",
                },
                {
                    "name": "test",
                    "description": "test",
                    "package": "test",
                    "module": "test",
                    "function": "test",
                },
            ],
            "output_target": "CODE",
            "output_path_uses_data_source_package": True,
            "output_file_prefix": "test",
            "output_file_name": "test",
            "output_file_suffix": "test",
            "output_file_extension": "test",
        },
    ],
}

TEST_DATA_REQUIRED = {
    "name": "test",
    "data_source": "test",
    "templates": [
        {
            "name": "test",
            "template_file": "test",
            "overwrite": "OVERWRITE",
            "output_target": "CODE",
            "output_file_extension": "test",
        },
        {
            "name": "test",
            "template_file": "test",
            "overwrite": "OVERWRITE",
            "output_target": "CODE",
            "output_file_extension": "test",
        },
    ],
}


class TestGeneratorSource(unittest.TestCase):
    def test_generatorsource_from_dict_all_fields(self):
        generatorsource_dict = TEST_DATA_ALL
        instance = GeneratorSource.from_dict(deepcopy(generatorsource_dict))
        self.assertEqual(instance.name, generatorsource_dict["name"])
        self.assertEqual(instance.data_source, generatorsource_dict["data_source"])
        self.assertEqual(instance.data_content, generatorsource_dict["data_content"])
        self.assertIsNotNone(instance.templates)

        generatorsource_dict = TEST_DATA_REQUIRED
        instance = GeneratorSource.from_dict(deepcopy(generatorsource_dict))
        self.assertEqual(instance.name, generatorsource_dict["name"])
        self.assertEqual(instance.data_source, generatorsource_dict["data_source"])
        self.assertIsNotNone(instance.templates)


if __name__ == "__main__":
    unittest.main()
