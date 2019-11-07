from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class DescribeFileSystems(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationToken: str = None,
        FileSystemId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMountTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FileSystemId: str = None,
        MountTargetId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FileSystemId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
