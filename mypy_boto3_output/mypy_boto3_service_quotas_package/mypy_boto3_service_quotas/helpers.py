"Helper functions for service-quotas service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_service_quotas.client import Client
from mypy_boto3_service_quotas.paginator import (
    ListAWSDefaultServiceQuotasPaginator,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
    ListRequestedServiceQuotaChangeHistoryPaginator,
    ListServiceQuotaIncreaseRequestsInTemplatePaginator,
    ListServiceQuotasPaginator,
    ListServicesPaginator,
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
    Equivalent of `boto3.client('service-quotas')`, returns a correct type.
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
        return session.client("service-quotas", **kwargs)
    return boto3.client("service-quotas", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_aws_default_service_quotas_paginator(
    client: Client,
) -> ListAWSDefaultServiceQuotasPaginator:
    """
    Equivalent of `client.get_paginator('list_aws_default_service_quotas')`, returns a correct type.
    """
    return client.get_waiter("list_aws_default_service_quotas")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_requested_service_quota_change_history_paginator(
    client: Client,
) -> ListRequestedServiceQuotaChangeHistoryPaginator:
    """
    Equivalent of `client.get_paginator('list_requested_service_quota_change_history')`, returns a correct type.
    """
    return client.get_waiter("list_requested_service_quota_change_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_requested_service_quota_change_history_by_quota_paginator(
    client: Client,
) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
    """
    Equivalent of `client.get_paginator('list_requested_service_quota_change_history_by_quota')`, returns a correct type.
    """
    return client.get_waiter("list_requested_service_quota_change_history_by_quota")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_service_quota_increase_requests_in_template_paginator(
    client: Client,
) -> ListServiceQuotaIncreaseRequestsInTemplatePaginator:
    """
    Equivalent of `client.get_paginator('list_service_quota_increase_requests_in_template')`, returns a correct type.
    """
    return client.get_waiter("list_service_quota_increase_requests_in_template")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_service_quotas_paginator(client: Client) -> ListServiceQuotasPaginator:
    """
    Equivalent of `client.get_paginator('list_service_quotas')`, returns a correct type.
    """
    return client.get_waiter("list_service_quotas")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_services_paginator(client: Client) -> ListServicesPaginator:
    """
    Equivalent of `client.get_paginator('list_services')`, returns a correct type.
    """
    return client.get_waiter("list_services")
