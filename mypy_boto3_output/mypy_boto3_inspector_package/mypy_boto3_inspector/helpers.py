"Helper functions for inspector service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_inspector.client import Client
from mypy_boto3_inspector.paginator import (
    ListAssessmentRunAgentsPaginator,
    ListAssessmentRunsPaginator,
    ListAssessmentTargetsPaginator,
    ListAssessmentTemplatesPaginator,
    ListEventSubscriptionsPaginator,
    ListExclusionsPaginator,
    ListFindingsPaginator,
    ListRulesPackagesPaginator,
    PreviewAgentsPaginator,
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
    Equivalent of `boto3.client('inspector')`, returns a correct type.
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
        return session.client("inspector", **kwargs)
    return boto3.client("inspector", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_assessment_run_agents_paginator(
    client: Client,
) -> ListAssessmentRunAgentsPaginator:
    """
    Equivalent of `client.get_paginator('list_assessment_run_agents')`, returns a correct type.
    """
    return client.get_waiter("list_assessment_run_agents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_assessment_runs_paginator(client: Client) -> ListAssessmentRunsPaginator:
    """
    Equivalent of `client.get_paginator('list_assessment_runs')`, returns a correct type.
    """
    return client.get_waiter("list_assessment_runs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_assessment_targets_paginator(
    client: Client,
) -> ListAssessmentTargetsPaginator:
    """
    Equivalent of `client.get_paginator('list_assessment_targets')`, returns a correct type.
    """
    return client.get_waiter("list_assessment_targets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_assessment_templates_paginator(
    client: Client,
) -> ListAssessmentTemplatesPaginator:
    """
    Equivalent of `client.get_paginator('list_assessment_templates')`, returns a correct type.
    """
    return client.get_waiter("list_assessment_templates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_event_subscriptions_paginator(
    client: Client,
) -> ListEventSubscriptionsPaginator:
    """
    Equivalent of `client.get_paginator('list_event_subscriptions')`, returns a correct type.
    """
    return client.get_waiter("list_event_subscriptions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_exclusions_paginator(client: Client) -> ListExclusionsPaginator:
    """
    Equivalent of `client.get_paginator('list_exclusions')`, returns a correct type.
    """
    return client.get_waiter("list_exclusions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_findings_paginator(client: Client) -> ListFindingsPaginator:
    """
    Equivalent of `client.get_paginator('list_findings')`, returns a correct type.
    """
    return client.get_waiter("list_findings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_rules_packages_paginator(client: Client) -> ListRulesPackagesPaginator:
    """
    Equivalent of `client.get_paginator('list_rules_packages')`, returns a correct type.
    """
    return client.get_waiter("list_rules_packages")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_preview_agents_paginator(client: Client) -> PreviewAgentsPaginator:
    """
    Equivalent of `client.get_paginator('preview_agents')`, returns a correct type.
    """
    return client.get_waiter("preview_agents")
