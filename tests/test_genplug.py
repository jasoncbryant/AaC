import yaml
from unittest import TestCase
from jinja2 import Template

from aac.genplug import compile_templates
from aac.parser import parseStr


class TestGenPlug(TestCase):
    def test_compile_templates(self):
        parsed_model = parseStr(TEST_PLUGIN_YAML_STRING, "", True)
        print()
        generated_templates = compile_templates(parsed_model)
        for template_name in generated_templates:
            print(f"----- {template_name} -----")
            print(generated_templates.get(template_name))


TEST_PLUGIN_YAML_STRING = """
data:
  name: Specification
  fields:
    - name: name
      type: string
    - name: description
      type: string
    - name: subspecs
      type: string[]
    - name: sections
      type: SpecSection[]
    - name: requirements
      type: Requirement[]
  required:
    - name
---
data:
  name: SpecSection
  fields:
    - name: name
      type: string
    - name: description
      type: string
    - name: requirements
      type: Requirement[]
  required:
    - name
---
data:
  name: Requirement
  fields:
    - name: id
      type: string
    - name: shall
      type: string
    - name: parent
      type: string
    - name: attributes
      type: RequirementAttribute[]
  required:
    - id
    - shall
---
data: 
  name: RequirementAttribute
  fields:
    - name: name
      type: string
    - name: value
      type: string
  required:
    - name
    - value
---
ext:
  name: addSpecificationToRoot
  type: root
  dataExt:
    add:
      - name: spec
        type: Specification
---
model:
  name: aac-spec
  description: aac-spec is a Architecture-as-Code plugin that enables requirement definition and trace in Arch-as-Code models.
  behavior:
    - name: spec-validate
      type: command
      description: Validates spec traces within the AaC model
      input:
        - name: archFile
          type: file
        - name: parsed_model
          type: map
      acceptance:
        - scenario: Valid spec traces are modeled.
          given:
            - The {{spec-validate.input.archFile}} contains a valid architecture specification.
            - The {{spec-validate.input.parsed_model}} contains the parsed content from archFile.
          when:
            - The aac app is run with the spec-validate command.
          then:
            - A message saying spec validation was successful is printed to the console.
  
"""
