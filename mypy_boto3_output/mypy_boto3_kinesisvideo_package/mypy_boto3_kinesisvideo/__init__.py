"Main interface for kinesisvideo service"

from mypy_boto3_kinesisvideo.client import Client
from mypy_boto3_kinesisvideo.helpers import boto3_client, get_list_streams_paginator


__all__ = ("Client", "boto3_client", "get_list_streams_paginator")
