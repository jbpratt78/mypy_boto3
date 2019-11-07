from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListDeploymentJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFleets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRobotApplications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRobots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSimulationApplications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSimulationJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
