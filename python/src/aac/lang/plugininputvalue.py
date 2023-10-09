"""Python module for the PluginInputValue class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators


@dataclass(frozen=True)
class PluginInputValue:
    """
    A value provided for a plugin input.

    name: str - The name of the plugin input being provided.
    value: str - The value of the plugin input being provided.
    """

    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    value: str = attrib(init=attr.ib(), validator=validators.instance_of(str))

    @classmethod
    def from_dict(cls, data):
        args = {}

        return cls(**args, **data)
