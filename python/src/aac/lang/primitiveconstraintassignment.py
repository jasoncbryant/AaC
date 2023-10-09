"""Python module for the PrimitiveConstraintAssignment class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators

from aac.lang.plugininputvalue import PluginInputValue


@dataclass(frozen=True)
class PrimitiveConstraintAssignment:
    """
    Assigns a primitive constraint to a primitive definition.

    name: str - The name of the schema constraint definition.
    arguments: list[PluginInputValue]] - Arguments for the primitive constraint if applicable.
    """

    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    arguments: list[PluginInputValue] = attrib(
        init=attr.ib(), validator=validators.instance_of(list[PluginInputValue])
    )

    @classmethod
    def from_dict(cls, data):
        args = {}

        arguments_data = data.pop("arguments", [])
        arguments = [PluginInputValue.from_dict(entry) for entry in arguments_data]
        args["arguments"] = arguments

        return cls(**args, **data)
