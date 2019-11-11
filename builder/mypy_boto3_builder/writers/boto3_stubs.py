from pathlib import Path

from mypy_boto3_builder.constants import README_PATH
from mypy_boto3_builder.structures import Boto3Module
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template


def write_boto3_stubs_module(boto3_module: Boto3Module, output_path: Path) -> None:
    module_path = output_path / boto3_module.package_name
    render_jinja2_template(
        output_path / "setup.py",
        Path("boto3-stubs") / "setup.py.jinja2",
        module=boto3_module,
        long_description=README_PATH.read_text() if README_PATH.exists() else "",
    )
    for file_name in [
        "py.typed",
        "__init__.pyi",
        "session.pyi",
        "__init__.py",
        "version.py",
    ]:
        render_jinja2_template(
            module_path / file_name,
            Path("boto3-stubs") / "boto3-stubs" / f"{file_name}.jinja2",
            module=boto3_module,
        )
