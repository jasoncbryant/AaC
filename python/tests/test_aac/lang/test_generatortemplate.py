# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

import unittest
from copy import deepcopy
from aac.lang.generatortemplate import GeneratorTemplate

TEST_DATA_ALL = {
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
}

TEST_DATA_REQUIRED = {
    "name": "test",
    "template_file": "test",
    "overwrite": "OVERWRITE",
    "output_target": "CODE",
    "output_file_extension": "test",
}


class TestGeneratorTemplate(unittest.TestCase):
    def test_generatortemplate_from_dict_all_fields(self):
        generatortemplate_dict = TEST_DATA_ALL
        instance = GeneratorTemplate.from_dict(deepcopy(generatortemplate_dict))
        self.assertEqual(instance.name, generatortemplate_dict["name"])
        self.assertEqual(instance.description, generatortemplate_dict["description"])
        self.assertEqual(
            instance.template_file, generatortemplate_dict["template_file"]
        )
        self.assertIsNotNone(instance.overwrite)
        self.assertIsNotNone(instance.helper_functions)
        self.assertIsNotNone(instance.output_target)
        self.assertEqual(
            instance.output_path_uses_data_source_package,
            generatortemplate_dict["output_path_uses_data_source_package"],
        )
        self.assertEqual(
            instance.output_file_prefix, generatortemplate_dict["output_file_prefix"]
        )
        self.assertEqual(
            instance.output_file_name, generatortemplate_dict["output_file_name"]
        )
        self.assertEqual(
            instance.output_file_suffix, generatortemplate_dict["output_file_suffix"]
        )
        self.assertEqual(
            instance.output_file_extension,
            generatortemplate_dict["output_file_extension"],
        )

        generatortemplate_dict = TEST_DATA_REQUIRED
        instance = GeneratorTemplate.from_dict(deepcopy(generatortemplate_dict))
        self.assertEqual(instance.name, generatortemplate_dict["name"])
        self.assertEqual(
            instance.template_file, generatortemplate_dict["template_file"]
        )
        self.assertIsNotNone(instance.overwrite)
        self.assertIsNotNone(instance.output_target)
        self.assertEqual(
            instance.output_file_extension,
            generatortemplate_dict["output_file_extension"],
        )


if __name__ == "__main__":
    unittest.main()
