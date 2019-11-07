from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class AnyInstanceInService(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceDeregistered(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceInService(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
