from pathlib import Path

# Master module name
MODULE_NAME = "mypy_boto3"

# PyPI module name
PYPI_NAME = "mypy-boto3"

# Random region to initialize services
DUMMY_REGION = "us-west-2"

# Jinja2 templates for boto3-stubs
TEMPLATES_PATH = Path(__file__).parent / "templates"

# Boto3 stubs module name
BOTO3_STUBS_NAME = "boto3-stubs"

# Jinja2 templates for boto3-stubs
README_PATH = Path(__file__).parent.parent.parent / "README.md"
