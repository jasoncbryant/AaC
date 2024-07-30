"""General purpose steps for the behave BDD tests."""""
from behave import given, when, then, use_step_matcher
import os
import json
from aac.execute.command_line import cli, initialize_cli
from aac.context.language_context import LanguageContext
from click.testing import CliRunner
from typing import Tuple

use_step_matcher("cfparse")


def get_model_file(context, path: str) -> str:
    """
    Retrieve the full path to the given model file.

    Args:
        context: Active context to check against.
        path (str): Path to the model file being evaluated.

    Return:
        Valid path for the requested model file as tracked within the context.
    """
    return os.path.sep.join([context.config.paths[0], path])


def run_cli_command_with_args(command_name: str, args: list[str]) -> Tuple[int, str]:
    """
    Invoke the CLI command with the given arguments.

    Args:
        command_name (str): CLI command to be executed.
        args (list[str]): List of arguments associated with the CLI command.

    Return:
        Exit code and output message resulting from the execution of the CLI command.
    """
    initialize_cli()
    runner = CliRunner()
    result = runner.invoke(cli, [command_name] + args)
    exit_code = result.exit_code
    std_out = str(result.stdout)
    output_message = std_out.strip().replace("\x1b[0m", "")
    return exit_code, output_message


@given('I have the "{model_file}" model')
def given_model(context, model_file: str):
    """
    Ensure the given model file exists.

    Args:
        context: Active context to check against.
        model_file (str): Path to the model file being evaluated.
    """
    print(f"DEBUG:  given model {model_file}")
    model_path = get_model_file(context, model_file)
    if not os.path.exists(model_path):
        raise AssertionError(f"Model file {model_path} does not exist")


@when('I check the "{model_file}" model')
def check_model(context, model_file):
    """
    Run the check command on the given model.

    Args:
        context: Active context to check against.
        model_file (str): Path to the model file being evaluated.
    """
    exit_code, output_message = run_cli_command_with_args(
        "check", [get_model_file(context, model_file)]
    )
    if exit_code != 0:
        raise AssertionError(f"Check cli command failed with message: {output_message}")
    context.output_message = output_message


@then("I should receive a message that the check was successful")
def check_success(context):
    """
    Ensure the check command was successful.

    Args:
        context: Active context to check against.
    """
    if "All AaC constraint checks were successful." not in context.output_message:
        raise AssertionError(
            f"Model check failed with message: {context.output_message}"
        )


@when(u'I load the "{model_file}" model')
def load_model(context, model_file):
    """
    Load a model file and put it into the context.
    
    Args:
        context: Active context to check against.
        model_file: Path of model file to load.
    """
    try:
        aac_context = LanguageContext()
        model_path = get_model_file(context, model_file)
        definitions = aac_context.parse_and_load(model_path)
        context.aac_loaded_definitions = definitions
    except Exception as e:
        raise AssertionError(f"Failed to load model file {model_file} with exception {e}")


@then(u'I should have {count} total {root_key} definitions')
def check_count_by_root_key(context, count, root_key):
    """
    Evaluate the number of root_key items parsed from a model.
    
    Args:
        context: Active context to check against.
        count: The number of definitions loaded from the model.
        root_key:  The root_key for the definitions of interest.
    """
    items = []
    for definition in context.aac_loaded_definitions:
        if definition.get_root_key() == root_key:
            items.append(definition)

    if len(items) != int(count):
        raise AssertionError(
            f"Found {len(items)} with root_key {root_key}, but expected {count}."
        )


@then(u'I should have requirement id {req_id}')
def check_req_id(context, req_id):
    """
    Evaluate the expected req ids are present in the parsed items.

    Args:
        context: Active context to check against.
        req_id_list: A list of req id values.
    """
    print("DEBUG: running 'I should have requirement ids' step_impl for {req_id}")
    parsed_ids = []
    for definition in context.aac_loaded_definitions:
        if definition.get_root_key() == "req":
            parsed_ids.append(definition.instance.id)
    if req_id not in parsed_ids:
        raise AssertionError(f"Expected id {req_id} not found in parsed req ids.")
