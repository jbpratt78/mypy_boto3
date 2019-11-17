"Main interface for devicefarm service"

from mypy_boto3_devicefarm.client import Client
from mypy_boto3_devicefarm.helpers import (
    boto3_client,
    get_get_offering_status_paginator,
    get_list_artifacts_paginator,
    get_list_device_instances_paginator,
    get_list_device_pools_paginator,
    get_list_devices_paginator,
    get_list_instance_profiles_paginator,
    get_list_jobs_paginator,
    get_list_network_profiles_paginator,
    get_list_offering_promotions_paginator,
    get_list_offering_transactions_paginator,
    get_list_offerings_paginator,
    get_list_projects_paginator,
    get_list_remote_access_sessions_paginator,
    get_list_runs_paginator,
    get_list_samples_paginator,
    get_list_suites_paginator,
    get_list_tests_paginator,
    get_list_unique_problems_paginator,
    get_list_uploads_paginator,
    get_list_vpce_configurations_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_offering_status_paginator",
    "get_list_artifacts_paginator",
    "get_list_device_instances_paginator",
    "get_list_device_pools_paginator",
    "get_list_devices_paginator",
    "get_list_instance_profiles_paginator",
    "get_list_jobs_paginator",
    "get_list_network_profiles_paginator",
    "get_list_offering_promotions_paginator",
    "get_list_offering_transactions_paginator",
    "get_list_offerings_paginator",
    "get_list_projects_paginator",
    "get_list_remote_access_sessions_paginator",
    "get_list_runs_paginator",
    "get_list_samples_paginator",
    "get_list_suites_paginator",
    "get_list_tests_paginator",
    "get_list_unique_problems_paginator",
    "get_list_uploads_paginator",
    "get_list_vpce_configurations_paginator",
)
