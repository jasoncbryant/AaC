"""Python module for the PrimitiveConstraintAssignment class."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators


@dataclass(frozen=True)
class PrimitiveConstraintAssignment:
    """
    Autogenerated PrimitiveConstraintAssignment AaC schema

    name: str - The name of the schema constraint definition.
    arguments: list[str] - A list of arguments to pass to the constraint.
    """

    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    arguments: list[str] = attrib(
        init=attr.ib(), validator=validators.instance_of(list[str])
    )

    @classmethod
    def from_dict(cls, data):
        args = {}

        arguments = data.pop("arguments", [])
        args["arguments"] = arguments

        return cls(**args, **data)
