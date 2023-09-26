from dataclasses import dataclass
import attr
from typing import Optional
from attr import attrib, validators
from aac.execute.aac_execution_result import LanguageError
from aac.lang.generatoroutputtarget import GeneratorOutputTarget

@dataclass(frozen=True)
class GeneratorTemplate():
    name: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    description: Optional[str] = attrib(init=attr.ib(), validator=validators.optional(validators.instance_of(str)))
    template_file: str = attrib(init=attr.ib(), validator=validators.instance_of(str))
    overwrite: bool = attrib(init=attr.ib(), validator=validators.instance_of(bool))
    output_target: GeneratorOutputTarget = attrib(init=attr.ib(), validator=validators.instance_of(GeneratorOutputTarget))

    @classmethod
    def from_dict(cls, data):
        description = None
        if "description" in data:
            description = data.pop("description")
        return cls(description=description, **data)
