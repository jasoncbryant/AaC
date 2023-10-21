"""The AaC Root schema must have name plugin implementation module."""
# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.

# There may be some unused imports depending on the definition of the plugin...but that's ok
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
)
from aac.lang.schema import Schema
from aac.lang.plugininputvalue import PluginInputValue
from aac.context.language_context import LanguageContext
from aac.context.definition import Definition
from aac.context.source_location import SourceLocation
from typing import Any


plugin_name = "Root schema must have name"


def root_schema_has_name(
    instance: Any, definition: Definition, defining_schema: Schema
) -> ExecutionResult:
    """Business logic for the Root schema has name constraint."""

    
    status = ExecutionStatus.SUCCESS
    messages: list[ExecutionMessage] = []
    
    if isinstance(instance, Schema):
        if instance.root:
            if len([field.name for field in instance.fields if field.name == "name"]) == 0:
                status = ExecutionStatus.GENERAL_FAILURE
                error_msg = ExecutionMessage(
                message=f"Root schema {instance.name} must have a field named 'name'",
                    source=definition.source,
                    location=None)
                messages.append(error_msg)

    return ExecutionResult(plugin_name, "Root schema has name", status, messages)
