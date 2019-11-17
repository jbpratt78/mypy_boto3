"Helper functions for datasync service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_datasync.client import Client
from mypy_boto3_datasync.paginator import (
    ListAgentsPaginator,
    ListLocationsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('datasync')`, returns a correct type.
    """
    kwargs = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("datasync", **kwargs)
    return boto3.client("datasync", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_agents_paginator(client: Client) -> ListAgentsPaginator:
    """
    Equivalent of `client.get_paginator('list_agents')`, returns a correct type.
    """
    return client.get_waiter("list_agents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_locations_paginator(client: Client) -> ListLocationsPaginator:
    """
    Equivalent of `client.get_paginator('list_locations')`, returns a correct type.
    """
    return client.get_waiter("list_locations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_waiter("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_task_executions_paginator(client: Client) -> ListTaskExecutionsPaginator:
    """
    Equivalent of `client.get_paginator('list_task_executions')`, returns a correct type.
    """
    return client.get_waiter("list_task_executions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tasks_paginator(client: Client) -> ListTasksPaginator:
    """
    Equivalent of `client.get_paginator('list_tasks')`, returns a correct type.
    """
    return client.get_waiter("list_tasks")
