# WARNIG - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED
# This file is auto-generated by aac gen-plugin and may be overwritten.

import aac
from aac.AacCommand import AacCommand
from aac_plantuml_impl import puml_component, puml_sequence, puml_object


@aac.hookimpl
def get_commands():
    ret_val = []
    ret_val.append(AacCommand(
        "puml-component",
        '''
        Converts an AaC model to Plant ULM component diagram
        ''', puml_component)
    )

    ret_val.append(AacCommand(
        "puml-sequence",
        '''
        Converts an AaC usecase to Plant ULM sequence diagram
        ''', puml_sequence)
    )

    ret_val.append(AacCommand(
        "puml-object",
        '''
        Converts an AaC model to Plant ULM object diagram
        ''', puml_object)
    )
    return ret_val
