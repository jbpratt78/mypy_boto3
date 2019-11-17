"Main interface for dms service"

from mypy_boto3_dms.client import Client
from mypy_boto3_dms.helpers import (
    boto3_client,
    get_describe_certificates_paginator,
    get_describe_connections_paginator,
    get_describe_endpoint_types_paginator,
    get_describe_endpoints_paginator,
    get_describe_event_subscriptions_paginator,
    get_describe_events_paginator,
    get_describe_orderable_replication_instances_paginator,
    get_describe_replication_instances_paginator,
    get_describe_replication_subnet_groups_paginator,
    get_describe_replication_task_assessment_results_paginator,
    get_describe_replication_tasks_paginator,
    get_describe_schemas_paginator,
    get_describe_table_statistics_paginator,
    get_endpoint_deleted_waiter,
    get_replication_instance_available_waiter,
    get_replication_instance_deleted_waiter,
    get_replication_task_deleted_waiter,
    get_replication_task_ready_waiter,
    get_replication_task_running_waiter,
    get_replication_task_stopped_waiter,
    get_test_connection_succeeds_waiter,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_certificates_paginator",
    "get_describe_connections_paginator",
    "get_describe_endpoint_types_paginator",
    "get_describe_endpoints_paginator",
    "get_describe_event_subscriptions_paginator",
    "get_describe_events_paginator",
    "get_describe_orderable_replication_instances_paginator",
    "get_describe_replication_instances_paginator",
    "get_describe_replication_subnet_groups_paginator",
    "get_describe_replication_task_assessment_results_paginator",
    "get_describe_replication_tasks_paginator",
    "get_describe_schemas_paginator",
    "get_describe_table_statistics_paginator",
    "get_endpoint_deleted_waiter",
    "get_replication_instance_available_waiter",
    "get_replication_instance_deleted_waiter",
    "get_replication_task_deleted_waiter",
    "get_replication_task_ready_waiter",
    "get_replication_task_running_waiter",
    "get_replication_task_stopped_waiter",
    "get_test_connection_succeeds_waiter",
)
